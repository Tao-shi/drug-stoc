# Terraform Infrastructure for Load-Balanced Web Servers and Database

This Terraform project provisions a scalable infrastructure on AWS, including:
- A load balancer.
- Two web servers running Nginx.
- A database server (MySQL).
- Security group/firewall rules allowing HTTP/HTTPS and SSH access.

The infrastructure is modular, reusable, and follows Terraform best practices.

## Infrastructure Overview

The infrastructure consists of the following components:

1. Load Balancer:
- Distributes traffic across the two web servers.
- Listens on HTTP (port 80).

2. Web Servers:
- Two EC2 instances running Nginx.
- Hosted in a public subnet.

3. Database Server:
- An RDS instance running MySQL.
- Hosted in a private subnet for security.

4. Security Groups:
- Allow HTTP/HTTPS and SSH access.

## Prerequisites
Before using this Terraform project, ensure you have the following:

1. Terraform Installed:
- Download and install Terraform.

2. AWS Account:
- Create an AWS account and configure your credentials using the AWS CLI or environment variables.

3. AWS CLI (Optional):
- Install the AWS CLI and configure it with your credentials:
`aws configure`

4. Remote Backend (Optional):
- Set up an S3 bucket and DynamoDB table for remote state storage.

## Direcroy Structure

terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
└── modules/
    ├── load_balancer/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── web_server/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── database/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── security_group/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf


## Setup Instructions

1. Clone the Repository:
`git clone <repository-url>`
`cd terraform`

2. Initialize Terraform:
`terraform init`

3. Review the Execution Plan:
`terraform plan`

4. Apply the Configuration:
`terraform apply` 

5. Destroy the Infrastructure (When Done):
`terraform destroy`


## Variables
The following variables are defined in root dir's variables.tf and can be customized in terraform.tfvars:

| Variable | Description	Default Value |
| ----------- | ----------- |
|aws_region	|AWS region for resources	us-east-1|
|instance_type	|EC2 instance type for web servers	t2.micro|
|db_username	|Database username |
|db_password	|Database password |
|backend_bucket	|S3 bucket for remote state storage	(Required)|
|backend_key	|Path to state file in S3 bucket	(Required)|
|backend_region	|AWS region for S3 bucket	(Required)|
|dynamodb_table	|DynamoDB table for state locking	(Required)|

Ensure that these variables are provided accordingly.