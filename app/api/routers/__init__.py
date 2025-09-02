from .reservas import router as reservas_router
from .usuarios import router as usuarios_router
from .restaurantes import router as restaurantes_router
from .cartas import router as cartas_router
from .platillos import router as platillos_router
from .mesas import router as mesas_router
from .auth import router as auth_router

__all__ = [
    "reservas_router",
    "usuarios_router",
    "restaurantes_router",
    "cartas_router",
    "platillos_router",
    "mesas_router",
    "auth_router",
]
