source app/venv/bin/activate
create python -m venv ./venv


aiokafka, fastapi, uvicorn

 uvicorn main:app --reload 

# Kafka Integration with Python
Docker based event driven application using Kafka to send and recieve real time messages.

## Features

- Send messages using kafka
- Recieve messages using kafka
- View messages using kafdrop

`(Ideally, a demo video should be put here.)`

<img width="1409" alt="Screenshot 2023-11-09 at 7 17 12 PM" src="https://github.com/beinghaziq/awesome-readme/assets/72576839/c884958c-f0dd-4ae1-bdcc-39a888cddcb8">


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
