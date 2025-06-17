# csv-crud-fastapi-docker
CSV CRUD with FastAPI and Docker is a project developed with Python.
The project show how to make a web-service for managing CSV data, using FastAPI and Docker.

The project is divided into four main steps:

1. **Development Environment Setup**
* Setting up Python environment using Anaconda.
* Integrate with GitHub.
* Configuring the workspace in Visual Studio Code using a requirements.txt file for the dependencies management.

2. **CRUD Web service development**
* Implement endpoints with FastAPI for the CSV file operations.
* Supported operations and API endpoints: 
    - CREATE: create a new record.
        `POST /items/`          
    - READ: get all the records.
        `GET /items/`
    - READ: get a record searched by id.
        `GET /items/{id}`
    - UPDATE: update a record searched by id.
        `PUT /items/{id}`
    - DELETE: delete a record searched by id.
        `DELETE /items/{id}`
    - COUNT: count all records.
        `GET /items/count`

3. **Create a Docker image**
* Create a Dockerfile for the FastAPI project.
* Use the Dockerfile to create a Docker image, that include the FastAPI web-service.

4. **Endpoint testing**
* Use Postman to verify that the endpoints are working.

## Dependencies
* FastAPI, version 0.115.12, to build APIs.
* Uvicorn, version 0.34.3, to run the web-server.
* Pydantic, version 2.11.5, to handle records.

## Installation
1. **Clone the repository and change directory**
* ```bash 
    git clone https://github.com/diegocapo04/csv-crud-fastapi-docker.git 
* ```bash
    cd csv-crud-fastapi-docker
2. **Create and activate the Anaconda environment**
* ```bash 
    conda create -n project python=3.11.13
* ```bash
    conda activate project
3. **Install dependencies**
* ```bash
    pip install -r requirements.txt
4. **Run the FastAPI server**
* ```bash
    uvicorn main:app --reload

## Docker
To build and run the project using Docker:
1. **Build the image**
* ```bash
    docker build -t csv-crud-fastapi .
2. **Run the container**
* ```bash
    docker run -p 8000:8000 csv-crud-fastapi