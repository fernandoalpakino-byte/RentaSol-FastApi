from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from datetime import datetime

from app.database.database import get_session
from app.models import MesasReservadas, Restaurante, Usuario
from app.schemas.reservas import ReservaCreate, ReservaRead

router = APIRouter(prefix="/restaurantes/{idrestaurante}/reservas", tags=["reservas"])

@router.post("", response_model=ReservaRead, status_code=status.HTTP_201_CREATED)
def crear_reserva(idrestaurante: str, payload: ReservaCreate, session: Session = Depends(get_session)):
    restaurante = session.get(Restaurante, idrestaurante)
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    usuario = session.get(Usuario, payload.idusuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    reserva = MesasReservadas(
        idrestaurante=idrestaurante,
        idusuario=payload.idusuario,
        fechadereserva=payload.fechadereserva,
        montoabonado=payload.montoabonado,
        estado="pendiente"
    )
    session.add(reserva)
    session.commit()
    session.refresh(reserva)
    return ReservaRead(
        idreserva=reserva.idreserva,
        idrestaurante=reserva.idrestaurante,
        idusuario=reserva.idusuario,
        fechadereserva=reserva.fechadereserva,
        montoabonado=reserva.montoabonado,
        estado=reserva.estado,
    )
