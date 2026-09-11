from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.utils.logging import error_logger

class LegalAssistantException(Exception):
    """Base exception for legal assistant services."""
    def __init__(self, message: str, status_code: int = 400, details: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

class DocumentNotFoundError(LegalAssistantException):
    def __init__(self, doc_id: str):
        super().__init__(f"Document with ID '{doc_id}' was not found.", status_code=404)

class ChunkNotFoundError(LegalAssistantException):
    def __init__(self, chunk_id: str):
        super().__init__(f"Chunk with ID '{chunk_id}' was not found.", status_code=404)

class RetrievalError(LegalAssistantException):
    def __init__(self, message: str):
        super().__init__(f"Retrieval error: {message}", status_code=500)

class LLMInferenceError(LegalAssistantException):
    def __init__(self, message: str):
        super().__init__(f"LLM inference error: {message}", status_code=502)

async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler converting unhandled exceptions to standardized JSON responses."""
    if isinstance(exc, LegalAssistantException):
        error_logger.warning(f"Handled error on {request.url.path}: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "message": exc.message,
                "details": exc.details,
                "path": request.url.path
            }
        )
    elif isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "message": exc.detail,
                "path": request.url.path
            }
        )
    else:
        error_logger.error(f"Unhandled exception on {request.url.path}: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "An internal server error occurred.",
                "details": str(exc),
                "path": request.url.path
            }
        )
