from fastapi import HTTPException
from sqlmodel import Session
from app.models import MesasReservadas
from app.schemas.reservas import ReservaCreate, ReservaRead
from app.repositories.reservas_repository import ReservasRepository

class ReservasService:
    def __init__(self, session: Session):
        self.repo = ReservasRepository(session)

    def crear_reserva(self, idrestaurante: str, payload: ReservaCreate) -> ReservaRead:
        restaurante = self.repo.get_restaurante(idrestaurante)
        if not restaurante:
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")

        usuario = self.repo.get_usuario(payload.idusuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        reserva = MesasReservadas(
            idrestaurante=idrestaurante,
            idusuario=payload.idusuario,
            fechadereserva=payload.fechadereserva,
            montoabonado=payload.montoabonado,
            estado="pendiente"
        )
        reserva = self.repo.crear_reserva(reserva)
        return ReservaRead(
            idreserva=reserva.idreserva,
            idrestaurante=reserva.idrestaurante,
            idusuario=reserva.idusuario,
            fechadereserva=reserva.fechadereserva,
            montoabonado=reserva.montoabonado,
            estado=reserva.estado,
        )
