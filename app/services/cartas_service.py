from fastapi import HTTPException
from sqlmodel import Session
from app.models import Carta
from app.schemas.cartas import CartaCreate, CartaRead
from app.repositories.cartas_repository import CartasRepository

class CartasService:
    def __init__(self, session: Session):
        self.repo = CartasRepository(session)

    def crear(self, payload: CartaCreate) -> CartaRead:
        carta = Carta(**payload.model_dump())
        carta = self.repo.crear(carta)
        return CartaRead(**carta.model_dump())

    def listar(self):
        cartas = self.repo.obtener_todas()
        return [CartaRead(**c.model_dump()) for c in cartas]

    def obtener(self, idcarta: str) -> CartaRead:
        carta = self.repo.obtener_por_id(idcarta)
        if not carta:
            raise HTTPException(status_code=404, detail="Carta no encontrada")
        return CartaRead(**carta.model_dump())

    def actualizar(self, idcarta: str, payload: CartaCreate) -> CartaRead:
        carta = self.repo.obtener_por_id(idcarta)
        if not carta:
            raise HTTPException(status_code=404, detail="Carta no encontrada")
        data = payload.model_dump()
        for k, v in data.items():
            setattr(carta, k, v)
        carta = self.repo.actualizar(carta)
        return CartaRead(**carta.model_dump())

    def eliminar(self, idcarta: str) -> None:
        carta = self.repo.obtener_por_id(idcarta)
        if not carta:
            raise HTTPException(status_code=404, detail="Carta no encontrada")
        self.repo.eliminar(carta)
