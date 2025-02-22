import os
import shutil
import psutil
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

 # Provide slack app api token to variable app_token
client = WebClient(token=app_token)
channel = "test-alert"
service_to_monitor = "ssh.service"
hostname = os.uname().nodename

THRESHOLDS = {
    "cpu_percent": 11,  # CPU usage threshold (%)
    "memory_percent": 0,  # Memory usage threshold (%)
    "disk_percent": 0,  # Disk usage threshold (%)
}

def restart_block(service):
    message = f"♻️ *{service}* was down and hass been restarted on *{hostname}*"
    return [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": message
			}
		},
		{
			"type": "divider"
		}
	]
    
def mem_high_block(val):
    message = f"🚨 Memory usage on *{hostname}* is HIGH: *{val}*%"
    return [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": message
			}
		},
		{
			"type": "divider"
		}
	]
def cpu_high_block(val):
    message = f"🚨 CPU usage on *{hostname}* is HIGH: *{val}*%"

    return [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": message
			}
		},
		{
			"type": "divider"
		}
	]
  
def disk_high_block(val):
    message = f"🚨 Disk usage on *{hostname}* is HIGH: *{val}*%"    
    return [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": message
			}
		},
		{
			"type": "divider"
		}
	]
def check_cpu_usage():
    """Check CPU usage."""
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def check_memory_usage():
    """Check memory usage."""
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk_usage():
    """Check disk usage."""
    disk = shutil.disk_usage("/")
    return (disk.used / disk.total) * 100

def check_service_status(service_name):
    """Check if a service is running and returns True or False"""
    try:
        output = os.popen(f"systemctl is-active {service_name}").read().strip()
        return output == "active"
    except Exception as e:
        print(f"Error checking service status: {e}")
        return False

def restart_service(service_name):
    """Restart service."""
    try:
        os.system(f"sudo systemctl restart {service_name}")
        print(f"Restarted {service_name}.")
    except Exception as e:
        print(f"Error restarting service: {e}")

def send_slack_notification(block):
    """Send a Slack notification."""
    try:
        response = client.chat_postMessage(
            channel=channel, 
            text="Default message.",  # Fallback text
            blocks=block
        )
        print("Message sent successfully: ", response["ts"])
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")


def main():
    # Check resource usage
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()

    # Check if service is running
    if not check_service_status(service_to_monitor):
        print(f"{service_to_monitor} is down. Restarting...")
        restart_service(service_to_monitor)
        send_slack_notification(restart_block(service_to_monitor))

    # Check thresholds and send alerts
    if cpu_usage > THRESHOLDS["cpu_percent"]:
         send_slack_notification(cpu_high_block(cpu_usage))
    if memory_usage > THRESHOLDS["memory_percent"]:
        send_slack_notification(mem_high_block(memory_usage))
    if disk_usage > THRESHOLDS["disk_percent"]:
        send_slack_notification(disk_high_block(disk_usage))

if __name__ == "__main__":
    main()