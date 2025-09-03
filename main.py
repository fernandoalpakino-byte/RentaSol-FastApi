from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import List

# Importar desde la nueva estructura
from app.database import create_db_and_tables, create_seed_data
from app.models import Usuario
from app.database.database import engine
from app.core.config import settings
from sqlmodel import Session, select

# Routers
from app.api.routers import (
    reservas_router,
    usuarios_router,
    restaurantes_router,
    cartas_router,
    platillos_router,
    mesas_router,
    auth_router,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Función de ciclo de vida de la aplicación"""
    create_db_and_tables()
    create_seed_data()
    yield

# Crear la aplicación FastAPI
app = FastAPI(
    title=settings.app.app_name,
    description="API para gestión de restaurantes y reservas de mesas",
    version=settings.app.app_version,
    lifespan=lifespan,
    debug=settings.app.debug
)

# Incluir routers
app.include_router(auth_router)
app.include_router(reservas_router)
app.include_router(usuarios_router)
app.include_router(restaurantes_router)
app.include_router(cartas_router)
app.include_router(platillos_router)
app.include_router(mesas_router)

@app.get("/")
def read_root():
    """Endpoint raíz de la API"""
    return {
        "message": f"Bienvenido a {settings.app.app_name}",
        "version": settings.app.app_version,
        "environment": settings.app.environment,
        "status": "activo"
    }

@app.post("/usuarios-old")
def create_usuario(usuario: Usuario):
    """Crear un nuevo usuario (legacy demo, usar /usuarios)"""
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.get("/usuarios-old", response_model=List[Usuario])
def get_usuarios():
    """Obtener todos los usuarios (legacy demo, usar /usuarios)"""
    with Session(engine) as session:
        usuarios = session.exec(select(Usuario)).all()
        return usuarios

@app.get("/health")
def health_check():
    """Verificar el estado de la API"""
    return {
        "status": "healthy", 
        "message": "API funcionando correctamente",
        "environment": settings.app.environment,
        "version": settings.app.app_version
    }

@app.get("/config")
def get_config():
    """Obtener información de configuración (solo en desarrollo)"""
    if settings.app.environment == "development":
        return {
            "database": {
                "host": settings.database.host,
                "port": settings.database.port,
                "database": settings.database.database,
                "username": settings.database.username,
                # No mostrar la contraseña por seguridad
            },
            "jwt": {
                "algorithm": settings.jwt.algorithm,
                "access_token_expire_minutes": settings.jwt.access_token_expire_minutes,
            },
            "app": {
                "name": settings.app.app_name,
                "version": settings.app.app_version,
                "environment": settings.app.environment,
                "debug": settings.app.debug,
            }
        }
    return {"message": "Configuración no disponible en producción"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host=settings.host, 
        port=settings.port,
        log_level=settings.log_level.lower()
    )