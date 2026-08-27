from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    distance_km: float = Field(..., gt=0, le=500)
    passengers: int = Field(1, ge=1, le=8)
    hour_of_day: int = Field(12, ge=0, le=23)


class PredictResponse(BaseModel):
    duration_min: float


class FeedbackRequest(BaseModel):
    request_id: str
    actual_duration_min: float = Field(..., gt=0)
