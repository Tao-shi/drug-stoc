output "aws_defauldvpc_id" {
  value = aws_default_vpc.default.id
}

output "web_servers_public_ips" {
  value = module.web_servers.web_server_ips
}

output "default_subnet_1a_id" {
  value = aws_default_subnet.default_az1a.id
}

output "default_subnet_1b_id" {
  value = aws_default_subnet.default_az1b.id
}

output "drug_elb_dns" {
  value = module.lb.alb_dns
}

output "drug_db_endpoint" {
  value = module.db.db_endpoint
}