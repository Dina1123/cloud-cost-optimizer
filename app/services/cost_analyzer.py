def analyze_cost(monthly_cost: float):
    if monthly_cost > 1000:
        return {
            "recommendation": "Review idle VM instances and rightsize resources",
            "estimated_savings": monthly_cost * 0.2
        }
    return {
        "recommendation": "Your costs are within the expected range",
        "estimated_savings": 0.0}