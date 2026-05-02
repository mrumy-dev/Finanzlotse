from decimal import Decimal, ROUND_HALF_UP

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Finanzlotse Prediction Service",
    version="0.0.1",
    description="Category suggestions and simple monthly spending predictions."
)

CATEGORY_RULES = {
    "Groceries": ["migros", "coop", "aldi", "lidl", "denner", "supermarket"],
    "Transport": ["sbb", "zvv", "vbz", "uber", "parking", "fuel"],
    "Subscriptions": ["spotify", "netflix", "microsoft", "google", "apple"],
    "Learning": ["orell", "udemy", "coursera", "book", "schule"],
    "Income": ["payroll", "salary", "lohn", "wage"],
}


class HealthResponse(BaseModel):
    status: str
    service: str


class CategoryPredictionRequest(BaseModel):
    merchant: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=240)
    amount: Decimal | None = None


class CategoryPredictionResponse(BaseModel):
    category: str
    confidence: float
    reason: str


class SpendingPredictionRequest(BaseModel):
    category: str = Field(min_length=1, max_length=80)
    previous_months: list[Decimal] = Field(min_length=1, max_length=12)
    current_month_spend: Decimal = Decimal("0.00")


class SpendingPredictionResponse(BaseModel):
    category: str
    predicted_amount: Decimal
    trend: str
    confidence: float


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="UP", service="finanzlotse-prediction-service")


@app.post("/predict/category", response_model=CategoryPredictionResponse)
def predict_category(payload: CategoryPredictionRequest) -> CategoryPredictionResponse:
    haystack = f"{payload.merchant} {payload.description}".lower()

    if payload.amount is not None and payload.amount > 0:
        return CategoryPredictionResponse(
            category="Income",
            confidence=0.72,
            reason="Positive transaction amount usually indicates income."
        )

    for category, keywords in CATEGORY_RULES.items():
        match = next((keyword for keyword in keywords if keyword in haystack), None)
        if match is not None:
            return CategoryPredictionResponse(
                category=category,
                confidence=0.86,
                reason=f"Matched keyword '{match}' in merchant or description."
            )

    return CategoryPredictionResponse(
        category="Uncategorized",
        confidence=0.35,
        reason="No known merchant or description keyword matched."
    )


@app.post("/predict/spending", response_model=SpendingPredictionResponse)
def predict_spending(payload: SpendingPredictionRequest) -> SpendingPredictionResponse:
    previous_total = sum(payload.previous_months, Decimal("0.00"))
    average = previous_total / Decimal(len(payload.previous_months))
    latest = payload.previous_months[-1]
    predicted = ((average * Decimal("0.70")) + (latest * Decimal("0.30"))).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    if latest > average * Decimal("1.10"):
        trend = "increasing"
    elif latest < average * Decimal("0.90"):
        trend = "decreasing"
    else:
        trend = "stable"

    if payload.current_month_spend > predicted:
        predicted = payload.current_month_spend

    return SpendingPredictionResponse(
        category=payload.category,
        predicted_amount=predicted,
        trend=trend,
        confidence=0.68
    )
