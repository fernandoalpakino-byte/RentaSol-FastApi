from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import List

# Importar desde la nueva estructura
from app.database import create_db_and_tables, create_seed_data
from app.models import Usuario
from app.database.database import engine
from sqlmodel import Session, select

# Routers
from app.api.routers import reservas_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Función de ciclo de vida de la aplicación"""
    create_db_and_tables()
    create_seed_data()
    yield

# Crear la aplicación FastAPI
app = FastAPI(
    title="RentaSol FastAPI",
    description="API para gestión de restaurantes y reservas de mesas",
    version="1.0.0",
    lifespan=lifespan
)

# Incluir routers
app.include_router(reservas_router)

@app.get("/")
def read_root():
    """Endpoint raíz de la API"""
    return {
        "message": "Bienvenido a RentaSol FastAPI",
        "version": "1.0.0",
        "status": "activo"
    }

@app.post("/usuarios")
def create_usuario(usuario: Usuario):
    """Crear un nuevo usuario"""
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.get("/usuarios", response_model=List[Usuario])
def get_usuarios():
    """Obtener todos los usuarios"""
    with Session(engine) as session:
        usuarios = session.exec(select(Usuario)).all()
        return usuarios

@app.get("/health")
def health_check():
    """Verificar el estado de la API"""
    return {"status": "healthy", "message": "API funcionando correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)