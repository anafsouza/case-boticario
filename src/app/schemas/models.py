from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any


class HealthStatus(BaseModel):
    """
    Schema for health check responses.

    Attributes:
        status (str): Indicates the health status of the service. Usually "ok" or "unhealthy".
        detail (str): Optional additional information or diagnostics.
    """
    status: str = Field(..., example="ok")
    detail: str = Field(..., example="Service is running")

class PredictionRequest(BaseModel):
    """
    Schema for request body to fetch predictions for multiple customer codes.

    Attributes:
        model_name (str): Name of the model to retrieve predictions for.
        codes (List[str]): List of customer codes.
    """
    model_name: str = Field(..., example="fraud_model")
    codes: List[str] = Field(..., example=["123", "456", "789"])


class PredictionResponse(BaseModel):
    """
    Schema for response body containing a list of predictions.

    Attributes:
        predictions (List[Dict[str, Optional[Any]]]): 
            A list where each item maps a key (model_name:client_code) to its prediction result.
    """
    predictions: List[Dict[str, Optional[Any]]] = Field(
        ..., 
        example=[
            {"model_name:123": {"score": 0.98}}, 
            {"model_name:456": None}
        ]
    )
