# Finanzlotse

Personal Finance & Subscription Manager for importing expenses, tracking subscriptions, and warning users before they overspend.

This project is scoped for a third year Informatiker HF portfolio project: realistic enough to show business software skills, but still small enough to finish with clean architecture, tests, documentation, and visible Git progress.

## Core Features

- CSV import for bank transactions
- Transaction, category, budget, and subscription management
- Monthly spending charts and category reports
- Recurring subscription detection
- Budget warning system with scheduled checks
- Exchange-rate integration for foreign currency expenses
- Mock banking API integration for local development
- REST API documentation with OpenAPI
- Unit and integration tests
- Docker Compose setup for local development
- Kubernetes manifests for deployment practice

## Tech Stack

- Backend: Kotlin, Spring Boot, Spring Security, Spring Data JPA
- Frontend: Angular, TypeScript
- Prediction service: Python for category detection and spending prediction
- Database: PostgreSQL
- Local infrastructure: Docker Compose
- Deployment: Kubernetes manifests
- APIs: exchange-rate API and mock banking API

## Repository Layout

```text
.
├── backend/             # Kotlin Spring Boot REST API
├── frontend/            # Angular client
├── prediction-service/  # Python category/spending prediction service
├── infra/
│   ├── docker-compose/  # Local PostgreSQL and services
│   └── k8s/             # Kubernetes deployment version
└── docs/                # Project plan, architecture notes, Git workflow
```

## Local Development

Run the full local stack with Docker Compose:

```bash
docker compose --env-file .env.example -f infra/docker-compose/docker-compose.yml up --build
```

Services:

- Frontend: `http://localhost:4200`
- Backend: `http://localhost:8080`
- Swagger UI: `http://localhost:8080/swagger-ui.html`
- Prediction service: `http://localhost:8000`
- Mock banking API: `http://localhost:9090/accounts/demo/transactions`
- PostgreSQL: `localhost:5432`

Run backend tests:

```bash
mvn -f backend/pom.xml test
```

Run prediction service tests after installing the Python test dependencies:

```bash
cd prediction-service
pip install -e ".[test]"
pytest
```

## Employer Signal

The project demonstrates typical business application work: CRUD APIs, data modeling, authentication, reporting, background jobs, CSV import, API integrations, test coverage, and deployment basics.

## Documentation

- [Project Plan](docs/project-plan.md)
- [Git Workflow](docs/git-workflow.md)
