---
layout: post
title: Getting started with terraform for free using AWS
date: 2024-02-03 10:18:00
---

Terraform is a powerful tool that can help automatically provision various types of infrastructure for software projects. In this post we'll dive into what it is, why its useful and how to get started with a simple example using the free tier offering from AWS.

# What is terraform?

Terraform is an open-source infrastructure as code software tool created by HashiCorp. It enables users to define and provision infrastructure using a declarative configuration language. With Terraform, you can manage various resources such as virtual machines, networks, storage, and more across multiple cloud providers like AWS, Azure, and Google Cloud Platform, as well as on-premises environments. Its primary objective is to automate the deployment and management of infrastructure, allowing for efficient scalability, version control, and reproducibility of infrastructure configurations.

# Why is terraform useful?

Terraform is highly useful for several reasons:

1. **Infrastructure as Code (IaC)**: Terraform allows you to define your infrastructure using code, enabling you to version control, review, and collaborate on infrastructure changes in the same way as application code. This makes infrastructure provisioning more predictable, repeatable, and scalable.
2. **Multi-Cloud Provisioning**: Terraform supports multiple cloud providers, allowing you to manage infrastructure across various environments, including public clouds like AWS, Azure, and Google Cloud Platform, as well as private clouds and on-premises data centers. This flexibility reduces vendor lock-in and enables hybrid and multi-cloud strategies.
3. **Automation**: With Terraform, you can automate the deployment and management of infrastructure, reducing manual intervention, human error, and the time required for provisioning and scaling resources. This automation enhances efficiency and reliability in managing infrastructure.
4. **State Management**: Terraform maintains a state file that keeps track of the current state of your infrastructure. This state allows Terraform to understand what resources are currently deployed and to determine the changes needed to match the desired configuration. State management ensures that Terraform can accurately provision and manage resources without causing conflicts or unintended changes.
5. **Modularity and Reusability**: Terraform modules enable you to encapsulate and reuse infrastructure configurations, making it easier to manage complex environments. Modules promote modularity, allowing you to abstract common patterns and share infrastructure components across projects or teams.
6. **Scalability and Flexibility**: Terraform is designed to scale with your infrastructure needs, whether you're managing a small application or a large-scale distributed system. Its flexibility allows you to adapt to changing requirements and quickly provision resources as your application grows.

Overall, Terraform provides a powerful set of tools and capabilities for managing infrastructure, offering efficiency, consistency, and agility in provisioning and maintaining cloud and on-premises environments.

# Typical architecture of where it is used

Let's consider a typical web application architecture deployed on a cloud infrastructure like AWS. Here's a simplified example of such an architecture and where Terraform fits in:

1. **Frontend Layer**: This layer consists of the user interface components of the web application, typically hosted on a web server such as Apache HTTP Server or Nginx. The frontend serves static content (HTML, CSS, JavaScript) and communicates with the backend via HTTP requests.
2. **Backend Layer**: The backend layer handles business logic, data processing, and interaction with databases or other external services. It includes components like application servers (e.g., Node.js, Django, Flask) and databases (e.g., MySQL, PostgreSQL, MongoDB).
3. **Data Storage Layer**: This layer encompasses various data storage solutions required by the application, such as relational databases, NoSQL databases, object storage (e.g., Amazon S3), caching services (e.g., Redis), or message queues (e.g., Amazon SQS).
4. **Networking Infrastructure**: Networking components like virtual private clouds (VPCs), subnets, security groups, load balancers, and DNS configurations are necessary to ensure secure communication and high availability of the application.
5. **Identity and Access Management (IAM)**: IAM controls access to cloud resources, defining user roles, permissions, and policies to enforce security measures and limit unauthorized access.

Where Terraform fits in:

Terraform is used to provision and manage the underlying infrastructure components of the application architecture. It allows you to define the desired state of the infrastructure using Terraform configuration files (written in HashiCorp Configuration Language, or HCL) and then automatically create, modify, or delete resources to achieve that state.

For example, with Terraform, you can:

- Define the networking infrastructure, including VPCs, subnets, route tables, and security groups required for the application.
- Provision compute resources such as EC2 instances for the frontend and backend servers, and RDS instances for the database.
- Configure load balancers to distribute incoming traffic across multiple instances for scalability and fault tolerance.
- Set up IAM roles and policies to control access to AWS resources securely.
- Manage DNS records for the application domain using Route 53.

Overall, Terraform enables infrastructure-as-code practices, allowing you to version control your infrastructure configurations, automate deployment processes, and ensure consistency and repeatability across different environments, from development to production.


# Installation

I am running Linux Mint 21.3 and will outline the steps needed to set this up on my machine. 

Hashicorp has details on how to install terraform for different operating systems but for Linux the latest release was not present on the site they point you to (https://apt.releases.hashicorp.com). Instead, I followed the below.

1. Find the latest version number by visiting `https://www.terraform.io/downloads.html`.
2. Download the latest version of terraform
    ```
    wget https://releases.hashicorp.com/terraform/<version>
    terraform_<version>_linux_amd64.zip
    ```
4. Extract archive
    ```
    unzip terraform_<version>_linux_amd64.zip
    ```
5. Move the executable into a directory where executable will be found by system
    ```
    sudo mv terraform /usr/local/bin/
    ```
6. Test installation has been successful by running
    ```
    terraform --version
    ```

# Example using AWS Free Tier

As mentioned above terraform can be used to spin up infrastructure for a number of providers and even a server on site. This example will focus on using terraform to set up an EC2 instance on the free tier of AWS. 


1. You'll need to set up an AWS account.
2. First we need to set up an access key and secret key that allows terraform to communicate with our AWS account. Once set up, log into the console. In the search bar, type 'IAM' and select the first option.
   1. If you haven't already set up MFA.
   2. Go to 'Manage access keys'.
   3. Under 'Access keys' you may see none. If so click 'Create access key' accept the conditions and click 'Create access key'.
   4. A page should appear with your access key and secret key - download them as a csv so you have them for future reference.
   5. Click 'Done' and on the main page you should now see your access key listed.
3. Next we need to identify which free tier AMI (Amazon machine image) we want to spin up.
   1. Search for 'EC2' and select the top option.
   2. In the left pane select 'AMI Catalog' - this will show us all available Amazon Machine Images we could use for our EC2 instance. Look for one that's free tier eligible. In my case I chose the 'Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type'.
   3. Take note of the AMI number listed just below the name of the AMI which for me is 'ami-0cf10cdf9fcd62d37'.
4. Now lets find which instance type we want
   1. In the left pane select 'Instance Types' and in the 'Instance types' search bar add the filter for free tier eligible.
   2. In my case I only have one to choose from so mine will be 't2.micro'.
5. The final piece of info we need before starting on our terraform is the location we want the infrastructure hosted in.
   1. In the top right corner of the console next to your username there is a drop down of all possible locations.
   2. Choose one that most closely matches your current location - for me that is 'eu-west-2' (as I'm based on London).
6. Now we're ready to get started.
7. Create a file called `main.tf` - typically this file will be stored in a separate infrastructure repository and not with the code you want to deploy to the server.
8. We'll now walk through each piece of what the terraform file needs to spin up the EC2 instance.
   1. **Terraform Block**: First define the required Terraform version and provider information. This chunk specifies that this configuration requires the AWS provider from HashiCorp. The version constraint ("~> 4.36") indicates that any version equal to or greater than 4.36
   
        ```terraform
        terraform {
        required_providers {
            aws = {
            source  = "hashicorp/aws"
            version = "~> 4.36"
            }
        }
        }
        ```

    2. **Variable Block**: These blocks define variables aws_access_key and aws_secret_key, which will be used to store AWS access and secret keys.
    They specify the type of the variables as strings and provide descriptions for clarity.
        ```terraform
        # Define variables for AWS access key and secret key
        variable "aws_access_key" {
            type        = string
            description = "Type in your AWS access key"
        }
        variable "aws_secret_key" {
            type        = string
            description = "Type in your AWS secret key"
        }
        ```
     3. **Provider Block**: This block configures the AWS provider.
    It sets the AWS region to "eu-west-2" and uses the values stored in the variables aws_access_key and aws_secret_key for authentication.

        ```terraform
        # Configure provider
        provider "aws" {
            region     = "eu-west-2"
            access_key = var.aws_access_key
            secret_key = var.aws_secret_key
        }
        ```
    4. **Resource Block - aws_instance**: This block creates an EC2 instance resource named "example" using the specified AMI (ami-0264a899947b7d068) and instance type (t3.micro).

        ```terraform
        # Create aws_instance resource named 'example'
        resource "aws_instance" "example" {
            ami  = "ami-0264a899947b7d068" # amazon machine image
            instance_type = "t3.micro"
        }
        ```
     5. **Resource Block - aws_security_group**: This block creates a security group resource named "ec2_security_group" for EC2 instances.
    It specifies a name and description for the security group.
    Defines ingress rules to allow inbound SSH, HTTP, and HTTPS traffic, and an egress rule allowing all outbound traffic.
        ```terraform
        # EC2 instance Security Group
        resource "aws_security_group" "ec2_security_group" {
            name        = "ec2_security_group"
            description = "Allow SSH inbound traffic"
        
            # Allow SSH inbound for allowed IP addressess
            ingress {
                from_port   = 22
                to_port     = 22
                protocol    = "tcp"
                cidr_blocks = tolist([])
            }

            # TCP port 80 for HTTP
            ingress {
                from_port   = 80
                to_port     = 80
                protocol    = "tcp"
                cidr_blocks = ["0.0.0.0/0"] # allows all traffic
            }

            # TCP port 443 for HTTPS
            ingress {
                from_port   = 443
                to_port     = 443
                protocol    = "tcp"
                cidr_blocks = ["0.0.0.0/0"]
            }

            # Outbound HTTP to anywhere
            egress {
                from_port   = 0
                to_port     = 0
                protocol    = "-1"
                cidr_blocks = ["0.0.0.0/0"]
            }
        }
        ```

     6. **Resource Block - tls_private_key**:     This block generates an RSA private key of size 4096 bits using the TLS provider.
        ```terraform
        # Create RSA key of size 4096 bits
        resource "tls_private_key" "tf_ec2_key" {
            algorithm = "RSA"
            rsa_bits  = 4096
        }
        ```
    7. **Resource Block - local_file**: This block creates a local file named "tf_ec2_key.pem" containing the RSA private key generated in the previous block.
        ```terraform
        # Create local file
        resource "local_file" "tf_ec2_key" {
            content  = tls_private_key.tf_ec2_key.private_key_pem
            filename = "${path.module}/tf_ec2_key.pem"
        }
        ```
    8. **Resource Block - aws_key_pair**:     This block creates an AWS key pair resource named "tf_ec2_key" using the RSA public key generated previously.

        ```terraform
        # Create AWS key pair
            resource "aws_key_pair" "tf_ec2_key" {
            key_name   = "tf_ec2_key"
            public_key = tls_private_key.tf_ec2_key.public_key_openssh
        }

        ```


9. Putting this all together we get the below `main.tf` file

    ```terraform
    terraform {
        required_providers {
            aws = {
            source  = "hashicorp/aws"
            version = "~> 4.36"
            }
        }
    }

    # Define variables for AWS access key and secret key
    variable "aws_access_key" {
        type        = string
        description = "Type in your AWS access key"
    }
    variable "aws_secret_key" {
        type        = string
        description = "Type in your AWS secret key"
    }

    # Configure provider
    provider "aws" {
        region     = "eu-west-2"
        access_key = var.aws_access_key
        secret_key = var.aws_secret_key
    }

    # Create aws_instance resource named 'example'
    resource "aws_instance" "example" {
        ami  = "ami-0264a899947b7d068" # Where to find this?
        instance_type = "t3.micro"     # Where to find this?
    }

    # EC2 instance Security Group
    resource "aws_security_group" "ec2_security_group" {
        name        = "ec2_security_group"
        description = "Allow SSH inbound traffic"
        
        # Allow SSH inbound for allowed IP addressess
        ingress {
            from_port   = 22
            to_port     = 22
            protocol    = "tcp"
            cidr_blocks = tolist([])
        }

        # TCP port 80 for HTTP
        ingress {
            from_port   = 80
            to_port     = 80
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"] # allows all traffic
        }

        # TCP port 443 for HTTPS
        ingress {
            from_port   = 443
            to_port     = 443
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
        }

        # Outbound HTTP to anywhere
        egress {
            from_port   = 0
            to_port     = 0
            protocol    = "-1"
            cidr_blocks = ["0.0.0.0/0"]
        }
    }

    # Create RSA key of size 4096 bits
    resource "tls_private_key" "tf_ec2_key" {
        algorithm = "RSA"
        rsa_bits  = 4096
    }

    # Create local file
    resource "local_file" "tf_ec2_key" {
        content  = tls_private_key.tf_ec2_key.private_key_pem
        filename = "${path.module}/tf_ec2_key.pem"
    }

    # Create AWS key pair
    resource "aws_key_pair" "tf_ec2_key" {
        key_name   = "tf_ec2_key"
        public_key = tls_private_key.tf_ec2_key.public_key_openssh
    }
    ```

 10. We can test if this runs by running the following in a terminal in the location where `main.tf` is saved
        ```console
        terraform plan
        ```
11. You will be prompted to enter your values for access_key and access_secret as it runs. You can copy and paste these into the terminal window.
12. There is a better way to manage these variables rather than pasting them into a terminal window. If you set up a variables file named `terraform.tfvars` this will allow you to set values for vars that terraform can use at runtime.
    ```
    aws_secret_key = "YOUR_SECRET_KEY_VALUE"
    aws_access_key = "YOUR_ACCESS_KEY_VALUE"
    ```
    Now we can tell terraform to run with this vars file as follows
    ```
    terraform plan -var-file="terraform.tfvars"
    ```
13. If that runs without issue you can now actually execute the terraform code using `apply` and watch the magic happen in your AWS console
    ```
    terraform apply -var-file="terraform.tfvars"
    ```
14. You should now see a new EC2 instance appear in the location specified with the relevant AMI and instance type.

