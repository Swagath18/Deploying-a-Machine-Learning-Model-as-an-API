# ML API: End-to-End Deployment with FastAPI, Docker, GitHub Actions, and AWS EC2
This project showcases a complete machine learning pipeline for predicting healthcare claim attributes, deployed via a production-grade API using FastAPI, Docker, CI/CD, and AWS EC2.

## Project Overview
Goal: Predict whether a healthcare claim has a physical copy (has_physical_copy) based on patient and claim metadata.

## Tech Stack:

Python, Pandas, Scikit-learn
FastAPI + Uvicorn
Docker + Docker Hub
GitHub Actions for CI/CD
AWS EC2 for cloud deployment

## Project Architecture
```bash
Data Generation → Cleaning → Feature Engineering → Model Training
          ↓
     FastAPI for Prediction Endpoint
          ↓
   Dockerized & CI/CD via GitHub Actions
          ↓
   Deployed to EC2 & Served via Public IP
```
## Features
Synthetic healthcare claim dataset (2M+ simulated records)
Robust ETL: missing value handling, anonymization, validation
Logistic Regression model with one-hot encoding
FastAPI server with /predict endpoint
UI for easy testing
Dockerized application
GitHub Actions CI/CD pipeline
Fully deployed to public EC2 server

## Folder Structure
```bash
.
├── scripts/                  # Data generation
├── etl/                     # Cleaning & validation
├── models/                  # Feature engineering + model training
├── api/                     # FastAPI app + schema
├── notebooks/               # Data exploration
├── Dockerfile               # Image definition
├── requirements.txt         # Python dependencies
└── .github/workflows/       # CI/CD pipeline
```
## How to Run Locally
```bash
# Step 1: Generate and clean data
python scripts/generate_data.py
python etl/clean_data.py
python etl/validate_data.py
python models/feature_engineering.py


## Step 2: Train and save model
python models/train_model.py

# Step 3: Run FastAPI server
uvicorn api.main:app --reload
# Visit http://localhost:8000/docs
```

##  Dockerization
```bash
# Build and run locally
docker build -t project-ml-api .
docker run -p 8000:8000 project-ml-api
```
## GitHub Actions (CI/CD)
```bash
Build Docker image
Ready to extend with deployment stages
```
##  Dockerhub publishing
```bash
# dockerhub publishing
docker tag project-ml-api username/project-ml-api
docker login
docker push username/project-ml-api

```
## AWS EC2 Deployment
```bash
Launch EC2 Instance:
AMI: Ubuntu 24.04
Opened ports: 22, 8000, 80, 443
Key Pair: name1.pem

#SSH from Git Bash:
ssh -i name1.pem ubuntu@<your-ec2-public-ip>

# On EC2 (after SSH with p1.pem)
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
newgrp docker
docker --version

docker pull username/project-ml-api
docker run -d -p 8000:8000 username/project-ml-api

#Access your API:
Visit http://<ec2-ip>:8000/docs
#here <ec2-ip> is your EC2 instance public ipv4

```
##  Instance terminated after demo to avoid AWS charges.Shutdown (No Charges)
```bash
Terminate EC2 from AWS Console:
EC2 Dashboard → Select Instance → Instance State → Terminate
(Optional): Go to EC2 → Volumes → Delete if still attached
```

## Author
Swagath Babu
