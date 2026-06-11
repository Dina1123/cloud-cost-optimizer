from pydantic import BaseModel


class CostRequest(BaseModel):
    monthly_cost: float


class CostResponse(BaseModel):
    recommendation: str
    estimated_savings: float