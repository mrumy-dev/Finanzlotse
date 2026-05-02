# Docker Compose

Local development stack for Finanzlotse.

## Start

```bash
docker compose --env-file ../../.env.example -f infra/docker-compose/docker-compose.yml up --build
```

Services:

- Frontend: `http://localhost:4200`
- Backend: `http://localhost:8080`
- Backend Swagger UI: `http://localhost:8080/swagger-ui.html`
- Prediction service: `http://localhost:8000`
- Mock banking API: `http://localhost:9090`
- PostgreSQL: `localhost:5432`

