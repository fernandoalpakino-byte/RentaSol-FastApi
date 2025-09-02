from fastapi import APIRouter

api_router = APIRouter()

from .routers import reservas  # noqa: F401
