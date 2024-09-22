
# Backend | LAB1 | Prokhorenko Artem | IO-23

This is a simple Flask application that can be run using Docker. The application includes a health check endpoint (`/healthcheck`) that returns the current timestamp and service status.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Run Locally](#run-locally)
  - [Run with Docker](#run-with-docker)
  - [Run with Docker Compose](#run-with-docker-compose)
- [Endpoints](#endpoints)

## Prerequisites
Before you can run the application, ensure you have the following installed:
- Python 3.11 or newer
- Docker
- Docker Compose

## Setup Instructions

### Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\Activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   flask --app lab1 run --host=0.0.0.0 --port=5000
   ```

### Run with Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. Build the Docker image:
   ```bash
   docker build -t lab1_app:latest .
   ```

3. Run the Docker container:
   ```bash
   docker run -it --rm -p 5000:5000 -e PORT=5000 lab1_app:latest
   ```

### Run with Docker Compose
1. Build the image and run the container with Docker Compose:
   ```bash
   docker-compose build
   docker-compose up
   ```

2. The application will be accessible at:
   ```bash
   http://localhost:5000
   ```

## Endpoints

| Endpoint       | Description                              | Method |
| -------------- | ---------------------------------------- | ------ |
| `/healthcheck` | Returns the current timestamp and status | GET    |
