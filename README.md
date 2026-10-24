# AWS 3-Tier Architecture - Project 01

A feedback web application deployed on AWS using a three-tier design.

## Architecture
Users -> Internet Gateway -> Public ALB -> Nginx (web tier, public subnets)
-> Internal ALB -> Flask (app tier, private subnets) -> RDS MySQL (DB tier, private subnets)

![Architecture](docs/architecture.png)

## Components
- VPC 10.0.0.0/16 with 6 subnets across 2 AZs (ap-south-1a, ap-south-1b)
- Internet Gateway and NAT Gateway, 3 route tables
- Security groups chained tier by tier (alb-sg > web-sg > internal-alb-sg > app-sg > db-sg)
- Nginx reverse proxy (nginx.conf), Flask API (app.py), RDS MySQL 8.4

## How it was verified
Form submitted through the public ALB and stored in the RDS `feedback` table.
See docs/ for the full step-by-step report with screenshots.

## Notes
Secrets in app.py are placeholders. Auto Scaling (bonus) was not completed due to the account's vCPU limit.# AWS-3-Tier-Architecture---Project-01
