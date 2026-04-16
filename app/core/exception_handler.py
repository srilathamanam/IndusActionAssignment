from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.utils.api_response import api_failure_response

# Global exception handling
def global_exception_handler(request: Request, status: HTTPException):
    return JSONResponse(
        status_code=status,
        content=api_failure_response(
            message="Internal Server Error",
            status_code=500,
            error=str(status)
        )
    )