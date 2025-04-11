from fastapi import FastAPI
from app.config.health_checks import router as health_router
from api import api_v1

# Create the main FastAPI application instance
app = FastAPI(
    title="Health Check API",
    description="A basic FastAPI application with liveness and readiness endpoints.",
    version="1.0.0"
)

# Include the health check router
app.include_router(health_router)





api_response = {
    "entity": 123,
    "data": {
        # resposta do predict. ex:
        "prediction": 1,
        "pred_proba": 0.97,
        "extra_info": "any extra information the data scientist and user decide to add."
    },
    "modelname": "model_name",
    "specversion": "1.0.0",
    "datacontenttype": "application/json",
    "id": "8e420530-5e4e-4341-98ca-0317c8b0a105",
    "eventtype": "ml_model_output",
    "eventdate": "2025-04-09T15:40:42.002418",
}



