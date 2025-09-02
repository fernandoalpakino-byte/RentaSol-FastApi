from datetime import datetime, time
from pydantic import BaseModel, Field
from typing import Optional

class RestauranteBase(BaseModel):
    nombrelocal: str
    descripcion: str
    telefono: str
    direccion: str
    horadeapertura: time
    horadecierre: time
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    logo: Optional[str] = None
    idusuario: str

class RestauranteCreate(RestauranteBase):
    pass

class RestauranteRead(RestauranteBase):
    idrestaurante: str
    createdat: datetime
