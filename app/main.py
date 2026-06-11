from fastapi import FastAPI
from app.models.cost_models import (
    CostRequest,
    CostResponse
)

from app.services.cost_analyzer import analyze_cost

app = FastAPI(
    title="Cloud Cost Optimizer",
    version="0.1"
)


@app.get("/")
def root():
    return {
        "message": "Cloud Cost Optimizer API is running"
    }

@app.post(
    "/analyze",
    response_model=CostResponse
)
def analyze(request: CostRequest):
    result = analyze_cost(
        request.monthly_cost
    )

    return result