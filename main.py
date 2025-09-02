postgresql_uri = "postgresql+psycopg2://postgres:123456789@localhost:5432/c-labs-demo"

from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from datetime import datetime
from contextlib import asynccontextmanager
import uuid
from fastapi import FastAPI

def generate_uuid() -> str:
    return str(uuid.uuid4())

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    idusuario: str = Field(default_factory=generate_uuid, primary_key=True)
    nombre: str = Field(max_length=100, sa_column_kwargs={"nullable": False})
    apellido: str = Field(max_length=100, sa_column_kwargs={"nullable": False})
    ruc: Optional[str] = Field(default=None, max_length=15)
    correo: str = Field(max_length=100, sa_column_kwargs={"nullable": False, "unique": True})
    telefono: str = Field(max_length=100, sa_column_kwargs={"nullable": False})
    password: str = Field(max_length=300, sa_column_kwargs={"nullable": False})
    fechacreacion: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"nullable": False})
    tipousuario: str = Field(max_length=20, sa_column_kwargs={"nullable": False})  # guardamos como string

engine = create_engine(postgresql_uri, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/usuarios")
def create_usuario(usuario: Usuario):
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.get("/usuarios", response_model=List[Usuario])
def get_usuarios():
    with Session(engine) as session:
        usuarios = session.exec(select(Usuario)).all()
        return usuarios
