terraform {

  backend "s3" {
    bucket         = "terraform-state-bucket"    # Replace with your S3 bucket name
    key            = "path/to/terraform.tfstate" # Path to store the state file
    region         = "us-east-1"                 # Replace with your AWS region
    encrypt        = true                        # Encrypt the state file at rest
    dynamodb_table = "terraform-lock-table"      # Replace with your DynamoDB table name
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.77.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}

resource "aws_default_subnet" "default_az1a" {
  availability_zone = "us-east-1a"

  tags = {
    Name = "Default subnet for us-west-1a"
  }
}

resource "aws_default_subnet" "default_az1b" {
  availability_zone = "us-east-1b"

  tags = {
    Name = "Default subnet for us-west-1a"
  }
}


module "security_group" {
  source               = "./modules/security-groups"
  aws_default_vpc      = aws_default_vpc.default.id
  aws_default_vpc_cidr = aws_default_vpc.default.cidr_block

}

module "web_servers" {
  source                 = "./modules/web-servers"
  vpc_security_group_ids = [module.security_group.sg_id]
  ami                    = var.ami_id
  instance_name          = var.instance_name
  instance_type          = var.instance_type
  priv_key_name          = var.key_name
}

module "lb" {
  source             = "./modules/lb"
  security_group_ids = [module.security_group.sg_id]
  default_subnet     = [aws_default_subnet.default_az1a.id, aws_default_subnet.default_az1b.id]
  default_vpc_id     = aws_default_vpc.default.id
  webserver_id       = module.web_servers.instance_ids
}

module "db" {
  source             = "./modules/db"
  db_instance_type   = var.db_instance_type
  db_password        = var.db_password
  db_username        = var.db_username
  security_group_ids = [module.security_group.sg_id]

}