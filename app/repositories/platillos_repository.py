from typing import Optional, List
from sqlmodel import Session, select
from app.models import Platillo

class PlatillosRepository:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, platillo: Platillo) -> Platillo:
        self.session.add(platillo)
        self.session.commit()
        self.session.refresh(platillo)
        return platillo

    def obtener_todos(self) -> List[Platillo]:
        return self.session.exec(select(Platillo)).all()

    def obtener_por_id(self, idplatillo: str) -> Optional[Platillo]:
        return self.session.get(Platillo, idplatillo)

    def actualizar(self, platillo: Platillo) -> Platillo:
        self.session.add(platillo)
        self.session.commit()
        self.session.refresh(platillo)
        return platillo

    def eliminar(self, platillo: Platillo) -> None:
        self.session.delete(platillo)
        self.session.commit()
