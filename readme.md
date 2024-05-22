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
   git clone [<repository-url>](https://github.com/beinghaziq/kafka-with-python.git)
   cd repo
   create a .env file and copy content from .env.example to it
   ```
2. **Build the Docker Images**:
   ```bash
   docker-compose build
   ```
3. **Initialize the Database**:
   - Before starting the application for the first time, ensure that the database is set up correctly.
   ```bash
   docker-compose up -d db
   docker-compose run web rails db:create db:migrate
   ```
   - Now run the application with
   ```bash
   docker-compose up
   ```

## API Documentation
