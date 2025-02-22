resource "aws_instance" "web_server" {
  count         = 2
  ami           = var.ami
  instance_type = var.instance_type

  key_name               = var.priv_key_name
  vpc_security_group_ids = var.vpc_security_group_ids

  provisioner "remote-exec" {
    inline = [
      "sudo apt update -y",
      "sudo apt install -y nginx",
      "sudo systemctl start nginx",
      "sudo systemctl enable nginx"
    ]
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/Us-East-KP.pem")
    host        = self.public_ip
  }

  tags = {
    Name = "${var.instance_name}-${count.index + 1}"
  }
}