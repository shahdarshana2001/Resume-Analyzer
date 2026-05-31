# AI Resume Analyzer

AI Resume Analyzer is a backend application that demonstrates asynchronous resume processing using FastAPI, Celery, Redis, and Docker.

The application accepts resume data through a REST API, processes the analysis in the background using Celery workers, and allows users to retrieve the analysis results using a task identifier. This architecture simulates how modern AI and document-processing systems handle long-running workloads without blocking user requests.

The project identifies predefined technical skills from resume content, calculates basic resume statistics, and returns a structured analysis result. The application is designed using a scalable architecture where API handling, task processing, and message brokering are separated into independent components.

## Key Features

* REST API built with FastAPI
* Background task processing using Celery
* Redis-based message queue and result backend
* Dockerized Redis deployment
* Automatic API documentation with Swagger UI
* Resume skill extraction
* Resume word count analysis
* Asynchronous processing architecture
* Task status tracking using unique task IDs

## System Architecture

Client
   │
   ▼
FastAPI Application
   │
   ▼
Redis Message Broker
   │
   ▼
Celery Worker
   │
   ▼
Resume Analysis Engine
   │
   ▼
Analysis Result


## Technology Stack

### API Layer

* FastAPI
* Uvicorn

### Background Processing

* Celery

### Message Broker

* Redis

### Containerization

* Docker

### Data Validation

* Pydantic

### Dependency Management

* uv

## Application Workflow

1. A client submits resume information through the API.
2. FastAPI validates the request data.
3. The request is sent to a Celery task queue.
4. Redis stores and manages the task message.
5. A Celery worker retrieves the task and performs the analysis.
6. The analysis result is stored in Redis.
7. The client retrieves the result using the generated task ID.

This architecture enables the application to handle resource-intensive processing tasks without affecting API responsiveness and provides a foundation for future AI-powered resume analysis capabilities.
