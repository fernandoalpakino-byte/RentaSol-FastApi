from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class ReservaCreate(BaseModel):
    idusuario: str = Field(..., description="ID del usuario que reserva")
    fechadereserva: datetime = Field(..., description="Fecha y hora de la reserva (UTC)")
    montoabonado: float = Field(..., ge=0, description="Monto abonado por la reserva")

class ReservaRead(BaseModel):
    idreserva: str
    idrestaurante: str
    idusuario: str
    fechadereserva: datetime
    montoabonado: float
    estado: str
