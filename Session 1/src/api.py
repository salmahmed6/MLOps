from time import perf_counter
from uuid import uuid4

import structlog
from fastapi import FastAPI

from src.logging_config import configure_logging
from src.schemas import (
    FeedbackRequest,
    PredictRequest,
    PredictResponse,
)

app = FastAPI(
    title="Ride Duration ML Service",
    version="0.1.0",
)

configure_logging()
log = structlog.get_logger()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictResponse)
async def predict(data: PredictRequest) -> PredictResponse:
    request_id = str(uuid4())
    start = perf_counter()

    # Simple placeholder prediction.
    # We will replace this with the trained model later.
    duration = (
        data.distance_km * 4.5
        + data.passengers * 1.5
        + abs(data.hour_of_day - 12) * 0.1
    )

    latency_ms = (perf_counter() - start) * 1000

    log.info(
        "predict.success",
        request_id=request_id,
        endpoint="/predict",
        latency_ms=round(latency_ms, 3),
        distance_km=data.distance_km,
        passengers=data.passengers,
    )

    return PredictResponse(duration_min=round(duration, 2))


@app.post("/feedback")
async def feedback(data: FeedbackRequest) -> dict[str, str]:
    log.info(
        "feedback.received",
        request_id=data.request_id,
        endpoint="/feedback",
        actual_duration_min=data.actual_duration_min,
    )

    return {"status": "received"}
