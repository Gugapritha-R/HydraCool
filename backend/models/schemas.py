from pydantic import BaseModel, Field
from enum import Enum

class PredictRequest(BaseModel):

    weight: float = Field(..., gt=0)

    temperature: float

    humidity: float = Field(..., ge=0, le=100)

    mist_usage: float = Field(..., ge=0)

    last_drink_minutes: float = Field(..., ge=0)

    daily_intake: float = Field(..., ge=0)

    time_of_day_ratio: float = Field(..., ge=0, le=1)
    

class RiskLevel(str,Enum):
    low="low"
    moderate="moderate"
    high="high"
    critical="critical"


class PredictResponse(BaseModel):

    hydration_score: float = Field(...,ge=0,le=100)
    heat_stress_score: float =Field(...,ge=0,le=100)
    risk_level:RiskLevel
    next_drink_minutes:int = Field(...,ge=0)
    recommended_ml:int = Field (...,ge=0)




