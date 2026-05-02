# Prediction Service

FastAPI service for category suggestions and simple spending projections.

## Local Run

```bash
pip install -e ".[test]"
uvicorn app.main:app --reload --port 8000
```

Health endpoint:

```text
GET /health
```

Prediction endpoints:

```text
POST /predict/category
POST /predict/spending
```

