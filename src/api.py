import os
from fastapi import APIRouter
from app.schemas.models import PredictionRequest, PredictionResponse
from app.model_serving.get_client_data import get_predictions
from app.config.redis_connection import RedisClient


# Redis connection
host = os.getenv("REDIS_HOST")
password = os.getenv("REDIS_PASSWORD")

redis_client = RedisClient(host=host, password=password)

# Include the predict router
api_v1 = APIRouter()


@api_v1.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
async def fetch_predictions(request: PredictionRequest) -> PredictionResponse:
    """
    Retrieve predictions for a list of customer codes based on a specified model.

    This endpoint queries a Redis instance for prediction data stored under keys
    in the format `{model_name}:{code}`.

    Args:
        request (PredictionRequest): A request body containing the model name and list of customer codes.

    Returns:
        PredictionResponse: A dictionary mapping each code to its corresponding prediction data,
        or None if the key does not exist in Redis.
    """
    
    model_name = request.model_name
    codes = request.codes

    predictions = get_predictions(
        model_name=model_name,
        codes=codes,
        redis_client=redis_client
    )

    return PredictionResponse(predictions=predictions)
