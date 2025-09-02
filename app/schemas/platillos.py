from pydantic import BaseModel, Field

class PlatilloBase(BaseModel):
    idcategoria: str
    nombre: str
    descripcion: str
    precio: float = Field(..., ge=0)
    imageurl: str
    moneda: str = "pen"
    idcarta: str

class PlatilloCreate(PlatilloBase):
    pass

class PlatilloRead(PlatilloBase):
    idplatillo: str
