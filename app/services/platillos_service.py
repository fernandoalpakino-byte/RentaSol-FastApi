from fastapi import HTTPException
from sqlmodel import Session
from app.models import Platillo
from app.schemas.platillos import PlatilloCreate, PlatilloRead
from app.repositories.platillos_repository import PlatillosRepository

class PlatillosService:
    def __init__(self, session: Session):
        self.repo = PlatillosRepository(session)

    def crear(self, payload: PlatilloCreate) -> PlatilloRead:
        platillo = Platillo(**payload.model_dump())
        platillo = self.repo.crear(platillo)
        return PlatilloRead(**platillo.model_dump())

    def listar(self):
        platillos = self.repo.obtener_todos()
        return [PlatilloRead(**p.model_dump()) for p in platillos]

    def obtener(self, idplatillo: str) -> PlatilloRead:
        platillo = self.repo.obtener_por_id(idplatillo)
        if not platillo:
            raise HTTPException(status_code=404, detail="Platillo no encontrado")
        return PlatilloRead(**platillo.model_dump())

    def actualizar(self, idplatillo: str, payload: PlatilloCreate) -> PlatilloRead:
        platillo = self.repo.obtener_por_id(idplatillo)
        if not platillo:
            raise HTTPException(status_code=404, detail="Platillo no encontrado")
        data = payload.model_dump()
        for k, v in data.items():
            setattr(platillo, k, v)
        platillo = self.repo.actualizar(platillo)
        return PlatilloRead(**platillo.model_dump())

    def eliminar(self, idplatillo: str) -> None:
        platillo = self.repo.obtener_por_id(idplatillo)
        if not platillo:
            raise HTTPException(status_code=404, detail="Platillo no encontrado")
        self.repo.eliminar(platillo)
