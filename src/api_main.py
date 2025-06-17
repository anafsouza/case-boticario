from fastapi import FastAPI
from app.config.health_checks import router as health_router
from app.config.redirect_to_docs import redirect_to_docs
from api import api_v1

# Create the main FastAPI application instance
app = FastAPI(
    title="Model Store API",
    description="A basic FastAPI application for general model serving.",
    version="1.0.0",
    docs_url="/docs"
)

# Include the health check router
app.include_router(health_router)
app.include_router(redirect_to_docs)
app.include_router(api_v1)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api_main:app", host="0.0.0.0", port=5000, reload=True)



