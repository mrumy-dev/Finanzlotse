from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_service_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "UP",
        "service": "finanzlotse-prediction-service",
    }


def test_category_prediction_detects_groceries() -> None:
    response = client.post(
        "/predict/category",
        json={
            "merchant": "Migros",
            "description": "Weekly shopping",
            "amount": "-42.80",
        },
    )

    assert response.status_code == 200
    assert response.json()["category"] == "Groceries"
    assert response.json()["confidence"] > 0.8


def test_spending_prediction_uses_previous_months() -> None:
    response = client.post(
        "/predict/spending",
        json={
            "category": "Groceries",
            "previous_months": ["510.00", "535.00", "560.00"],
            "current_month_spend": "120.00",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["category"] == "Groceries"
    assert body["trend"] == "stable"
    assert float(body["predicted_amount"]) > 530
