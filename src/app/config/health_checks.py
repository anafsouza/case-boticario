from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Create a router for health check endpoints
router = APIRouter()


@router.get("/health", summary="General Health Check", tags=["Health"])
async def health_check():
    """
    General health check endpoint.

    This endpoint provides a basic status response to indicate that the service is up.
    It can be used for manual verification or general-purpose monitoring.

    Returns:
        JSONResponse: A JSON object with a key "status" and value "ok".
    """
    return JSONResponse(content={"status": "ok"})


@router.get("/health/liveness", summary="Liveness Probe", tags=["Health"])
async def liveness_probe():
    """
    Liveness probe endpoint.

    This endpoint is used to determine if the application process is running.
    If this returns a non-200 status, the orchestrator (e.g., Kubernetes) may
    restart the container or service.

    Returns:
        JSONResponse: A JSON object indicating the app is alive.
    """
    return JSONResponse(content={"status": "alive"})


@router.get("/health/readiness", summary="Readiness Probe", tags=["Health"])
async def readiness_probe():
    """
    Readiness probe endpoint.

    This endpoint is used to determine if the application is ready to handle requests.
    It is useful for checking if dependencies like databases or external services are available.

    In a real application, this would include checks like:
    - Database connectivity
    - Cache system availability
    - Third-party service status

    Returns:
        JSONResponse: A JSON object indicating the app is ready.
    """
    # Placeholder check — replace with actual dependency checks if needed
    return JSONResponse(content={"status": "alive"})
