from fastapi import APIRouter
from app.schemas.models import PredictionRequest, PredictionResponse
from app.model_serving.get_client_data import get_predictions

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
        client_codes=codes
    )

    return PredictionResponse(predictions=predictions)
