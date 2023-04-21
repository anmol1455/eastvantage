# main.py

import logging
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.routing import APIRoute
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.exc import IntegrityError
from models.address import Address
from utils.distance import calculate_distance
from routes.address import router as address_router


app = FastAPI(
    title="Address Book API",
    description="An API for creating, updating and deleting addresses.",
    version="0.1",
)

# Add middleware for SQLAlchemy DBSession
app.add_middleware(DBSessionMiddleware, db_url="sqlite:///https://extendsclass.com/sqlite/16a56bb")

# Add API routes
app.include_router(address_router)


# Override the default exception handler to return a plain text response for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


# Override the default exception handler to log database errors
@app.exception_handler(IntegrityError)
async def database_exception_handler(request, exc):
    logging.error(exc)
    return PlainTextResponse("Database error", status_code=500)


# Override the default APIRoute to add logging for API requests
class CustomAPIRoute(APIRoute):
    async def handle(self, request, call_next):
        logging.info(f"Received API request: {request.method} {request.url}")
        response = await super().handle(request, call_next)
        logging.info(f"Sent API response: {response.status_code}")
        return response


app.router.route_class = CustomAPIRoute
