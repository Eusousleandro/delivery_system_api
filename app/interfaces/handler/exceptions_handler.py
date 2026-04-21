from fastapi import Request
from fastapi.responses import JSONResponse

from app.domain.exceptions.exception import (
    CreatedonFailedException,
    NotFoundException,
    AlreadyExistsException,
    UpdatedonFailedException,
    DeletionFailedException
)

def register_exception_handlers(app):

    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc):
        return JSONResponse(
            status_code=404,
            content={"success": False, "message": "Resource not found"}
        )

    @app.exception_handler(AlreadyExistsException)
    async def already_exists_handler(request: Request, exc):
        return JSONResponse(
            status_code=400,
            content={"success": False, "message": "Resource already exists"}
        )

    @app.exception_handler(CreatedonFailedException)
    async def create_failed_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Error creating resource"}
        )

    @app.exception_handler(UpdatedonFailedException)
    async def update_failed_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Error updating resource"}
        )

    @app.exception_handler(DeletionFailedException)
    async def delete_failed_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Error deleting resource"}
        )

    @app.exception_handler(Exception)
    async def global_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Internal server error"}
        )