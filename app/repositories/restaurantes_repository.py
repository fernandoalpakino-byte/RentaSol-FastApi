from typing import Optional, List
from sqlmodel import Session, select
from app.models import Restaurante

class RestaurantesRepository:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, restaurante: Restaurante) -> Restaurante:
        self.session.add(restaurante)
        self.session.commit()
        self.session.refresh(restaurante)
        return restaurante

    def obtener_todos(self) -> List[Restaurante]:
        return self.session.exec(select(Restaurante)).all()

    def obtener_por_id(self, idrestaurante: str) -> Optional[Restaurante]:
        return self.session.get(Restaurante, idrestaurante)

    def actualizar(self, restaurante: Restaurante) -> Restaurante:
        self.session.add(restaurante)
        self.session.commit()
        self.session.refresh(restaurante)
        return restaurante

    def eliminar(self, restaurante: Restaurante) -> None:
        self.session.delete(restaurante)
        self.session.commit()
