provider "aws" {
  access_key = "AKIA6AUO2IJASIXNC3OH"
  secret_key = "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"
  region     = "ap-south-1"
}

# Create EC2 Instance
resource "aws_instance" "test-Amazon-Linux" {
  ami                         = "ami-079b5e5b3971bd10d"  # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  key_name                    = "bobur-key-Mumbai"
  user_data                   = "file(data.sh)"
  vpc_security_group_ids      = [aws_security_group.My_WebServerSecurity.id]

  # root disk
  root_block_device {
    volume_size           = "20"
    volume_type           = "gp2"
    delete_on_termination = true
  }

  # data disk
  ebs_block_device {
    device_name           = "/dev/xvda"
    volume_size           = "10"
    volume_type           = "gp2"
    delete_on_termination = true
  }

  tags = {
    Name    = "My Amazon Server"
    Owner   = "Bobur Urinboev"
    Project = "Terraform task-1"
  }
}

# Security Groups
resource "aws_security_group" "My_WebServerSecurity" {
  name        = "WebServerSecurityGroup"
  description = "Allow HTTP, HTTPS, SSH"

  dynamic "ingress" {
    for_each = ["443", "80"]
    content {
      description      = "TLS from VPC"
      from_port        = ingress.value
      to_port          = ingress.value
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
    }
  }

  ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name  = "Web Server SecurityGroup"
    Owner = "Bobur_Urinboev"
  }
}
