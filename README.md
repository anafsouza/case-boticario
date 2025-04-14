# FastAPI Project

A lightweight and modular API built with FastAPI, designed for scalability, clarity, and integration with tools like Docker, Redis, and Azure Pipelines.

## Features

- Modular architecture for maintainability and scalability
- Redis integration for caching or background processing
- Health check endpoints for monitoring
- Swagger documentation (auto-generated)
- Unit testing with `pytest`
- Docker support for containerization
- Azure Pipelines configuration for CI/CD

## Project Structure

This repository is organized as follows:

- `src/app/config/`  
  Contains configuration-related modules such as health checks and Redis connections.

- `src/app/model_serving/`  
  Contains logic for model data handling and service-specific operations.

- `src/app/schemas/`  
  Contains the data models used for request and response validation with Pydantic.

- `src/app/api_main.py`  
  Main FastAPI app instance with route registration.

- `src/app/api.py`  
  Optional file for routing or controller logic separation.

- `tests/`  
  Contains test cases to validate endpoints and app behavior.

- `requirements.txt`  
  List of dependencies required to run the API.

- `azure-pipelines.yml`  
  Azure DevOps pipeline configuration file for CI/CD automation.

- `Dockerfile`  
  Defines the Docker image for building and running the application.

- `.gitignore`  
  Specifies files and directories to be ignored by git.

- `README.md`  
  This file — overview and usage instructions.

- `CHANGELOG.md`  
  Track changes across versions.


## Running with Docker

- Build the image:

    ```bash
    docker build -t model-showcase .
    ```

- Run the container:

    ```bash
    docker run -d -p 0.0.0.0:5000:5000 model-showcase:latest
    ```

- Access the automatic documentation:

    ```
    http://0.0.0.0:5000/docs
    ```

## Local Installation

- Clone the repository and navigate into the root directory:

    ```bash
    git clone <repository-url>
    cd <project-name>
    ```

- Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate     # Linux/Mac
    venv\Scripts\activate        # Windows
    ```

- Install dependencies:

    ```bash
    pip install -r src/requirements.txt
    ```

- Run the application:

    ```bash
    uvicorn src.app.api_main:app --reload
    ```

## Running Tests

- Use `pytest` to run the unit tests:

    ```bash
    pytest tests/
    ```

## Continuous Integration

- This project uses **Azure Pipelines** for continuous integration.

- The `azure-pipelines.yml` file defines steps for:
    - Installing dependencies
    - Running tests
    - Optional build and publish steps

## Documentation

- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- Redis: https://redis.io/
- Docker: https://docs.docker.com/
- Azure Pipelines: https://learn.microsoft.com/en-us/azure/devops/pipelines/

## Version History

See [`CHANGELOG.md`](./CHANGELOG.md) for version history and release notes.

