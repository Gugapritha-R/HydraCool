from models.schemas import PredictRequest,PredictResponse,RiskLevel

def run_prediction(request_data:PredictRequest):

    hydration_score = 75
    heat_stress_score = 40
    risk_level = RiskLevel.moderate
    next_drink_minutes = 20
    recommended_ml = 150

    return PredictResponse(
        hydration_score=hydration_score,
        heat_stress_score=heat_stress_score,
        risk_level=risk_level,
        next_drink_minutes=next_drink_minutes,
        recommended_ml=recommended_ml
    )