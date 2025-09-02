from pydantic import BaseModel

class CartaBase(BaseModel):
    nombrecarta: str
    idcategoriacarta: str
    idrestaurante: str

class CartaCreate(CartaBase):
    pass

class CartaRead(CartaBase):
    idcarta: str
