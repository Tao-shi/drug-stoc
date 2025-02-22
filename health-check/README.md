# System Monitoring and Alerting App

This Python script monitors system resources (CPU, memory, and disk usage) and the status of a specified service (e.g., ssh.service). If any resource exceeds predefined thresholds or the service is down, it sends an alert to a Slack channel and automatically restarts the service if necessary.

## How It Works

### 1. Resource Monitoring:

- CPU Usage: Checks the current CPU usage percentage.

- Memory Usage: Checks the current memory usage percentage.

- Disk Usage: Checks the current disk usage percentage.

### 2. Service Monitoring:

- Checks if the specified service (e.g., ssh.service) is active.

- If the service is down, it automatically restarts the service.

### 3. Thresholds:

- The script uses predefined thresholds for CPU, memory, and disk usage. If any threshold is exceeded, it sends an alert to Slack.

### 4. Slack Notifications:

- Sends formatted Slack messages with alerts for:

** High CPU usage.
** High memory usage.
** High disk usage.
** Service restarts.

## Prerequisites

1. Python Libraries:

- Install the required libraries:
`pip install -r requirements` (slack_sdk and psutils)

2. Slack App:

- Create a Slack app and obtain an API token.
- Set the token in the script as app_token.

3. System Permissions:

- Ensure the script has permission to restart services (e.g., run with sudo).

## Configuration

- Thresholds: Update the THRESHOLDS dictionary in the script to set custom thresholds for CPU, memory, and disk usage.

- Service to Monitor: Set the service_to_monitor variable to the service you want to monitor (e.g., ssh.service).

- Slack Channel: Set the channel variable to the Slack channel where alerts should be sent.

## Usage

1. Run the script:

`python3 app.py`

2. The script will:

- Monitor system resources and service status.
- Send Slack alerts if thresholds are exceeded or the service is down.
- Restart the service if it is not active.

## Notes

Ensure the script runs continuously (e.g., using a cron job or a process manager like systemd).