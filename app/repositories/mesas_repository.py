from typing import Optional, List
from sqlmodel import Session, select
from app.models import Mesa

class MesasRepository:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, mesa: Mesa) -> Mesa:
        self.session.add(mesa)
        self.session.commit()
        self.session.refresh(mesa)
        return mesa

    def obtener_todas(self) -> List[Mesa]:
        return self.session.exec(select(Mesa)).all()

    def obtener_por_id(self, idmesa: str) -> Optional[Mesa]:
        return self.session.get(Mesa, idmesa)

    def actualizar(self, mesa: Mesa) -> Mesa:
        self.session.add(mesa)
        self.session.commit()
        self.session.refresh(mesa)
        return mesa

    def eliminar(self, mesa: Mesa) -> None:
        self.session.delete(mesa)
        self.session.commit()
