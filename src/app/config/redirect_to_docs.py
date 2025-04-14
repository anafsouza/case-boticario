from fastapi import APIRouter, responses

redirect_to_docs = APIRouter()

DOCS_ROUTE = "/docs"

@redirect_to_docs.get("/", include_in_schema=False)
async def docs_redirect():
    """
    Redirect default path to docs.
    """
    
    return responses.RedirectResponse(url=DOCS_ROUTE)

