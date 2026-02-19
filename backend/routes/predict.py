from fastapi import APIRouter
from models.schemas import PredictRequest,PredictResponse
from services.ai_service import run_prediction  

router = APIRouter()

@router.post("/predict",response_model=PredictResponse)
def predict(request: PredictRequest):
    return run_prediction(request)
    