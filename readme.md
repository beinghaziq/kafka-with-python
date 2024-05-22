# Kafka Integration with Python
Docker based event driven application using Kafka to send and recieve real time messages.

## Features

- Send messages using kafka
- Recieve messages using kafka
- View messages using kafdrop

<img width="997" alt="Screenshot 2024-05-21 at 5 55 39 PM" src="https://github.com/beinghaziq/kafka-with-python/assets/72576839/7f3aa139-4246-4b07-9d91-efcac9fd43fe">
<img width="1296" alt="Screenshot 2024-05-21 at 6 00 19 PM" src="https://github.com/beinghaziq/kafka-with-python/assets/72576839/c4f61162-7626-4e93-91b8-d9d25163a7b8">
<img width="1287" alt="Screenshot 2024-05-21 at 5 55 54 PM" src="https://github.com/beinghaziq/kafka-with-python/assets/72576839/a143e5bf-e033-44eb-8ab4-afc7a0d00beb">


# Build With

- Framework: Python 3.11
- Docker
- Kafka

# Getting Started

## Prerequisites

- Docker Desktop app
- python
- pip
(for new project)
- venv
```bash
  create python -m venv ./venv
  ```
- fastapi(in venv)
 ```bash
  pip install fastapi
  ```
- aiokafk(in venv)
 ```bash
  pip install fastapi
  ```
- uvicorn(in venv)
```bash
  pip install uvicorn
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/beinghaziq/kafka-with-python.git
   cd repo
   ```
2. **Build the Docker Images**:
    It will install kafka and related dependencies
   ```bash
   docker-compose up -d
   ```

3. **Setup VENV(optional)**:
   - setup virtual environment
   ```bash
    source app/venv/bin/activate
   ```

4. **Run Application**:
   - Run the application
   ```bash
    uvicorn main:app --reload 
   ```

## Miscellaneous
 - All dependencies can be added in requirements.txt and run using:
    ```bash
    pip install -r requirements.txt
   ```

## API Documentation

<img width="1219" alt="Screenshot 2024-05-21 at 6 44 12 PM" src="https://github.com/beinghaziq/kafka-with-python/assets/72576839/3364cd6d-6f73-434e-8c03-76c08771d599">

