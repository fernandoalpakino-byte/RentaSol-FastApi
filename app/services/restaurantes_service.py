from fastapi import HTTPException
from sqlmodel import Session
from app.models import Restaurante
from app.schemas.restaurantes import RestauranteCreate, RestauranteRead
from app.repositories.restaurantes_repository import RestaurantesRepository

class RestaurantesService:
    def __init__(self, session: Session):
        self.repo = RestaurantesRepository(session)

    def crear(self, payload: RestauranteCreate) -> RestauranteRead:
        restaurante = Restaurante(**payload.model_dump())
        restaurante = self.repo.crear(restaurante)
        return RestauranteRead(**restaurante.model_dump())

    def listar(self):
        restaurantes = self.repo.obtener_todos()
        return [RestauranteRead(**r.model_dump()) for r in restaurantes]

    def obtener(self, idrestaurante: str) -> RestauranteRead:
        restaurante = self.repo.obtener_por_id(idrestaurante)
        if not restaurante:
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")
        return RestauranteRead(**restaurante.model_dump())

    def actualizar(self, idrestaurante: str, payload: RestauranteCreate) -> RestauranteRead:
        restaurante = self.repo.obtener_por_id(idrestaurante)
        if not restaurante:
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")
        data = payload.model_dump()
        for k, v in data.items():
            setattr(restaurante, k, v)
        restaurante = self.repo.actualizar(restaurante)
        return RestauranteRead(**restaurante.model_dump())

    def eliminar(self, idrestaurante: str) -> None:
        restaurante = self.repo.obtener_por_id(idrestaurante)
        if not restaurante:
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")
        self.repo.eliminar(restaurante)
