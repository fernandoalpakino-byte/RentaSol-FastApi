from pydantic import BaseModel

class MesaBase(BaseModel):
    numeromesa: int
    capacidad: int
    estado: str
    qrcode: str
    restauranteid: str

class MesaCreate(MesaBase):
    pass

class MesaRead(MesaBase):
    idmesa: str
