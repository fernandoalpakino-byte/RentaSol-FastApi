from sqlmodel import create_engine, Session
from sqlmodel import SQLModel
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+psycopg2://postgres:123456789@localhost:5432/c-labs-demo"
)

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """Crear todas las tablas en la base de datos"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Obtener una sesión de base de datos"""
    with Session(engine) as session:
        yield session
