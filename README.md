# Flask Application with PostgreSQL (Dockerized)

This project is a simple Flask application that communicates with the OpenAI API and stores questions and answers in a PostgreSQL database. The application is fully Dockerized and can be run locally using `docker-compose`.

## Features

- Exposes a POST endpoint at `/ask` to receive questions, send them to OpenAI, and store responses.
- Uses PostgreSQL for storing questions and responses.
- Dockerized setup for easy deployment.
- Environment variables managed through a `.env` file.
- Database migrations handled by Flask-Migrate and Alembic.

## Getting Started

### Prerequisites

- **Docker**: Make sure you have Docker and Docker Compose installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/Ohadyk/QuestionsServer.git
cd QuestionsServer
```

### 2. Set Up Environment Variables
Create a .env file in the root of your project with the following content:

# Database Configuration
DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase

# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key
OPENAI_ORGANIZATION=your_openai_organization
OPENAI_PROJECT=your_openai_project

### 3. Build and Run the Application with Docker
To build the Docker containers and start the Flask and PostgreSQL services, run the following command:

`docker compose up -d`

This will:

Build the Flask application container.
Pull and start the official PostgreSQL container.
Connect the two containers using the docker-compose.yml configuration.

### 4. Access the Application
Once everything is up and running, you can access the Flask application at:

`http://localhost:5000`

# API Endpoints
POST /ask: Send a JSON payload with the key "question" to this endpoint to send the question to the OpenAI API and store the response in the PostgreSQL database.

`curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is Flask?"}'`

Response:

`{
  "question": "What is Flask?",
  "answer": "Flask is a micro web framework written in Python."
}`

### 5. Stopping the Application
To stop the running containers, use:

`docker compose down`

This will stop and remove the containers.

# Project Dependencies
The project uses the following Python libraries:

Flask

SQLAlchemy

alembic

openai

python-dotenv

pytest

psycopg2-binary

You can find all dependencies in the requirements.txt file.

# License
This project is licensed under the MIT License - see the LICENSE file for details.