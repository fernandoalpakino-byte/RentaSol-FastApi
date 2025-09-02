from typing import Optional, List
from sqlmodel import Session, select
from app.models import Carta

class CartasRepository:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, carta: Carta) -> Carta:
        self.session.add(carta)
        self.session.commit()
        self.session.refresh(carta)
        return carta

    def obtener_todas(self) -> List[Carta]:
        return self.session.exec(select(Carta)).all()

    def obtener_por_id(self, idcarta: str) -> Optional[Carta]:
        return self.session.get(Carta, idcarta)

    def actualizar(self, carta: Carta) -> Carta:
        self.session.add(carta)
        self.session.commit()
        self.session.refresh(carta)
        return carta

    def eliminar(self, carta: Carta) -> None:
        self.session.delete(carta)
        self.session.commit()
