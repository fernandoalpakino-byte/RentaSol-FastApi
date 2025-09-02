from typing import Optional
from sqlmodel import Session
from app.models import MesasReservadas, Restaurante, Usuario

class ReservasRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_restaurante(self, idrestaurante: str) -> Optional[Restaurante]:
        return self.session.get(Restaurante, idrestaurante)

    def get_usuario(self, idusuario: str) -> Optional[Usuario]:
        return self.session.get(Usuario, idusuario)

    def crear_reserva(self, reserva: MesasReservadas) -> MesasReservadas:
        self.session.add(reserva)
        self.session.commit()
        self.session.refresh(reserva)
        return reserva
