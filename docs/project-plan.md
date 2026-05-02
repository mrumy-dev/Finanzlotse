# Project Plan

## Goal

Build a personal finance application that helps users understand monthly spending, track recurring subscriptions, and react early when a budget is close to being exceeded.

The scope is intentionally realistic for a third year Informatiker HF student. The project should show practical engineering habits: small commits, readable code, tests, documentation, and a working local setup.

## Main User Stories

- As a user, I can import a CSV file with bank transactions.
- As a user, I can view, search, filter, and edit transactions.
- As a user, I can create categories and assign them to transactions.
- As a user, I can define monthly budgets per category.
- As a user, I receive warnings when spending reaches a budget threshold.
- As a user, I can see monthly spending charts.
- As a user, I can detect recurring subscriptions from transactions.
- As a user, I can convert foreign currency expenses with an exchange-rate API.
- As a developer, I can run the full system locally with Docker Compose.
- As a developer, I can inspect API documentation through OpenAPI.

## Domain Model

Core entities:

- User: account owner, authentication identity, preferences
- Transaction: date, amount, currency, merchant, description, category, source
- Category: user-defined or default spending group
- Budget: category, month, limit amount, warning threshold
- Subscription: merchant, estimated monthly amount, billing interval, next expected charge
- ImportJob: CSV import status, source file metadata, validation errors
- Alert: overspending or subscription warning shown to the user

## Backend Scope

The backend is a Kotlin Spring Boot REST API.

Main responsibilities:

- Expose CRUD endpoints for transactions, categories, budgets, and subscriptions
- Validate CSV import files and store import results
- Persist data in PostgreSQL through Spring Data JPA
- Protect endpoints with Spring Security
- Generate REST documentation with OpenAPI
- Run scheduled jobs for budget checks and subscription detection
- Call the Python prediction service when category suggestions are needed
- Call the exchange-rate API when a transaction is not in the user default currency

Suggested API groups:

- `/api/auth`
- `/api/transactions`
- `/api/categories`
- `/api/budgets`
- `/api/subscriptions`
- `/api/imports`
- `/api/reports`
- `/api/alerts`

## Frontend Scope

The frontend is an Angular application focused on daily finance workflows.

Main screens:

- Dashboard: monthly totals, budget warnings, subscription summary
- Transactions: import, filter, edit category, inspect details
- Budgets: create and adjust monthly category budgets
- Subscriptions: review detected recurring payments
- Reports: charts by month and category
- Settings: default currency and import preferences

The UI should be practical and business-like: dense enough for repeated use, clear tables, readable charts, and simple forms.

## Python Prediction Service

The Python service should stay small and explainable.

Initial version:

- Category detection based on merchant and description keywords
- Simple monthly spending prediction based on previous months
- REST endpoint consumed by the backend

Later improvement:

- Store learned merchant-category mappings
- Add confidence scores for category suggestions
- Compare predicted spending with configured budget limits

## Database

PostgreSQL is used in development and production-like deployment.

Important database concerns:

- Money values should use decimal types, not floating point
- Transaction imports should be idempotent where possible
- Index transactions by user, date, category, and merchant
- Store audit timestamps on business entities

## Integrations

Exchange-rate API:

- Used when imported transactions contain a currency different from the user's default currency
- Should be wrapped behind a backend service interface
- Should have mocked responses in tests

Mock banking API:

- Used for local development and demo data
- Provides a realistic external-system integration without requiring real banking credentials

## Scheduled Jobs

Scheduled jobs demonstrate backend business automation.

- Nightly budget check: creates warnings when spending exceeds 80 percent or 100 percent of a budget
- Weekly subscription detection: scans recent transactions for recurring merchant patterns
- Daily exchange-rate refresh: stores recent rates for supported currencies

## Testing Strategy

Backend:

- Unit tests for services, validators, and calculation logic
- Integration tests for REST endpoints and repositories
- Testcontainers or Docker Compose PostgreSQL for database-backed tests

Frontend:

- Component tests for forms and dashboard widgets
- Service tests for API clients
- A small number of end-to-end tests for the main workflow

Python:

- Unit tests for category rules and prediction functions
- Contract-style tests for service responses

## Milestones

### Milestone 1: Project Foundation

- Create repository structure
- Add backend, frontend, Python service, Docker Compose, and documentation placeholders
- Decide naming conventions and branch workflow

### Milestone 2: Backend Domain and Database

- Add Spring Boot project
- Configure PostgreSQL
- Implement entities, repositories, migrations, and basic CRUD endpoints
- Add OpenAPI setup

### Milestone 3: CSV Import and Transactions

- Implement CSV upload endpoint
- Validate rows and store import results
- Add transaction filtering and category assignment
- Add integration tests for import behavior

### Milestone 4: Angular Frontend Basics

- Scaffold Angular app
- Build transaction list and import screen
- Connect API client to backend
- Add basic dashboard layout

### Milestone 5: Budgets, Alerts, and Scheduled Jobs

- Add monthly budgets
- Implement budget warning calculation
- Add scheduled job for budget alerts
- Show warnings in frontend

### Milestone 6: Subscriptions and Reports

- Implement recurring subscription detection
- Add subscription review screen
- Add monthly spending charts
- Add report API tests

### Milestone 7: Prediction and API Integrations

- Add Python prediction service
- Connect category suggestions to backend
- Add exchange-rate and mock banking API integrations
- Add mocks and contract tests

### Milestone 8: Deployment and Final Polish

- Add Kubernetes manifests
- Improve README and API documentation
- Add final test coverage
- Prepare demo data and screenshots

