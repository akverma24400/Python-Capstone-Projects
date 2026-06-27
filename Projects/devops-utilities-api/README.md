# 🚀 DevOps Utilities API

A FastAPI-based DevOps utility application that provides APIs to monitor AWS resources and local system health.

## Features

* 📦 Amazon S3 Bucket Information
* 💻 Amazon EC2 Instance Information
* 💰 AWS Cost Explorer (Last 30 Days)
* 🖥️ System Health Monitoring (CPU, Memory & Disk Usage)
* 📖 Interactive API Documentation with Swagger

---

# Prerequisites

Before running the project, make sure you have:

* Python 3.10 or later
* Git
* An AWS Account
* AWS CLI installed

---

# 1. Fork and Clone the Repository

```bash
git clone https://github.com/<your-username>/devops-utilities-api.git
cd devops-utilities-api
```

---

# 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn boto3 psutil
```

---

# 4. Configure AWS Credentials

Install the AWS CLI (if not already installed), then run:

```bash
aws configure
```

Enter:

```text
AWS Access Key ID:
AWS Secret Access Key:
Default Region:
Default Output Format: json
```

---

# 5. Enable AWS Cost Explorer

If you want to use the **/cost** endpoint:

1. Log in to the AWS Console.
2. Open **Billing and Cost Management**.
3. Go to **Cost Explorer**.
4. Click **Enable Cost Explorer**.

> **Note:** It can take up to 24 hours for Cost Explorer data to become available after enabling it.

---

# 6. Grant Required IAM Permissions

Your IAM user or role should have permissions for:

* Amazon S3
* Amazon EC2
* AWS Cost Explorer (`ce:GetCostAndUsage`)

The easiest option is to attach the managed policy:

* **AWSBillingReadOnlyAccess**

---

# 7. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

If your `main.py` is in a different folder, update the command accordingly.

---

# 8. Open the API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Available Endpoints

| Method | Endpoint      | Description                           |
| ------ | ---------     | ------------------------------------- |
| GET    | `/aws/s3`     | Get S3 bucket information             |
| GET    | `/aws/ec2`    | Get EC2 instance information          |
| GET    | `/aws/cost`   | Get AWS cost for the last 30 days     |
| GET    | `/health`     | Get system CPU, Memory and Disk usage |
| GET    | `/logs`       | Get system logs.                      |

---

# Troubleshooting

### AWS Credentials Not Found

Run:

```bash
aws configure
```

---

### Access Denied

Ensure your IAM user has the required permissions, especially:

* `AmazonS3ReadOnlyAccess`
* `AmazonEC2ReadOnlyAccess`
* `AWSBillingReadOnlyAccess` (or `ce:GetCostAndUsage`)

---

### Cost Endpoint Returns an Error

* Ensure Cost Explorer is enabled.
* Wait up to 24 hours after enabling it.
* Verify your IAM user has Cost Explorer permissions.

---

## Author

**Akash Verma**

If you found this project useful, consider giving it a ⭐ on GitHub!
