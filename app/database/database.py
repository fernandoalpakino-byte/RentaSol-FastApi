from sqlmodel import create_engine, Session
from sqlmodel import SQLModel
from app.core.config import get_database_url, settings

# Configuración de la base de datos usando el sistema centralizado
DATABASE_URL = get_database_url()

# Crear el motor de la base de datos
# Solo mostrar SQL en modo debug
engine = create_engine(
    DATABASE_URL, 
    echo=settings.app.debug,
    pool_pre_ping=True,  # Verificar conexión antes de usar
    pool_recycle=3600,   # Reciclar conexiones cada hora
)

def create_db_and_tables():
    """Crear todas las tablas en la base de datos"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Obtener una sesión de base de datos"""
    with Session(engine) as session:
        yield session
