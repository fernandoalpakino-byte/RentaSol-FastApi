from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    ruc: Optional[str] = None
    correo: EmailStr
    telefono: str
    tipousuario: str

class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=6)

class UsuarioRead(UsuarioBase):
    idusuario: str
    fechacreacion: datetime

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    ruc: Optional[str] = None
    telefono: Optional[str] = None
    tipousuario: Optional[str] = None
