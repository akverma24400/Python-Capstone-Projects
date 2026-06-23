# DevOps Utilities API

A FastAPI-based DevOps utility service that provides system and AWS infrastructure information through REST APIs.

## Features

* System Metrics Monitoring

  * CPU Usage
  * Memory Usage
  * Disk Usage

* AWS Services Information

  * S3 Bucket Details
  * EC2 Instance Details
  * AWS Cost Information
  * Additional AWS utilities (extensible)

## Tech Stack

* Python
* FastAPI
* Boto3
* Psutil
* Uvicorn

## Prerequisites

* Python 3.10+
* AWS Account (for AWS-related endpoints)
* AWS CLI configured with appropriate permissions

## Installation

### 1. Fork and Clone the Repository

```bash
git clone https://github.com/<your-username>/devops-utilities-api.git
cd devops-utilities-api
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS Credentials

```bash
aws configure
```

Provide your:

* AWS Access Key ID
* AWS Secret Access Key
* Default Region
* Output Format

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

ReDoc Documentation:

```text
http://localhost:8000/redoc
```

## Available Endpoints

### Health Check

```http
GET /
```

### System Metrics

```http
GET /metrics
```

### S3 Bucket Information

```http
GET /aws/s3
```

### EC2 Instance Information

```http
GET /aws/ec2
```

### AWS Cost Information

```http
GET /aws/cost
```

## Sample Response

```json
{
  "instance_name": "Jenkins-Master",
  "instance_id": "i-0123456789abcdef0",
  "region": "ap-south-1",
  "status": "running"
}
```

## Future Enhancements

* CloudWatch Metrics
* RDS Information
* Lambda Monitoring
* ECS/EKS Insights
* Cost Optimization Recommendations

## Author

Akash Verma
