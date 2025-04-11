from fastapi import FastAPI
from health_checks import router as health_router
from schemas.models import PredictionRequest, PredictionResponse

# Create the main FastAPI application instance
app = FastAPI(
    title="Health Check API",
    description="A basic FastAPI application with liveness and readiness endpoints.",
    version="1.0.0"
)

# Include the health check router
app.include_router(health_router)


@app.post("/predict", response_model=PredictionResponse, summary="Get Predictions by Model and Codes", tags=["Predictions"])
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
    if not request.codes:
        raise HTTPException(status_code=400, detail="List of codes cannot be empty.")

    predictions = get_predictions(
        model_name=request.model_name,
        codes=request.codes,
        redis_client=redis_client
    )

    return PredictionResponse(predictions=predictions)
