from fastapi import HTTPException
from sqlmodel import Session
from app.models import Mesa
from app.schemas.mesas import MesaCreate, MesaRead
from app.repositories.mesas_repository import MesasRepository

class MesasService:
    def __init__(self, session: Session):
        self.repo = MesasRepository(session)

    def crear(self, payload: MesaCreate) -> MesaRead:
        mesa = Mesa(**payload.model_dump())
        mesa = self.repo.crear(mesa)
        return MesaRead(**mesa.model_dump())

    def listar(self):
        mesas = self.repo.obtener_todas()
        return [MesaRead(**m.model_dump()) for m in mesas]

    def obtener(self, idmesa: str) -> MesaRead:
        mesa = self.repo.obtener_por_id(idmesa)
        if not mesa:
            raise HTTPException(status_code=404, detail="Mesa no encontrada")
        return MesaRead(**mesa.model_dump())

    def actualizar(self, idmesa: str, payload: MesaCreate) -> MesaRead:
        mesa = self.repo.obtener_por_id(idmesa)
        if not mesa:
            raise HTTPException(status_code=404, detail="Mesa no encontrada")
        data = payload.model_dump()
        for k, v in data.items():
            setattr(mesa, k, v)
        mesa = self.repo.actualizar(mesa)
        return MesaRead(**mesa.model_dump())

    def eliminar(self, idmesa: str) -> None:
        mesa = self.repo.obtener_por_id(idmesa)
        if not mesa:
            raise HTTPException(status_code=404, detail="Mesa no encontrada")
        self.repo.eliminar(mesa)
