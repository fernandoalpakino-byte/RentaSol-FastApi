from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.database.database import get_session
from app.schemas.mesas import MesaCreate, MesaRead
from app.services.mesas_service import MesasService

router = APIRouter(prefix="/mesas", tags=["mesas"])

@router.post("", response_model=MesaRead, status_code=status.HTTP_201_CREATED)
def crear_mesa(payload: MesaCreate, session: Session = Depends(get_session)):
    return MesasService(session).crear(payload)

@router.get("", response_model=List[MesaRead])
def listar_mesas(session: Session = Depends(get_session)):
    return MesasService(session).listar()

@router.get("/{idmesa}", response_model=MesaRead)
def obtener_mesa(idmesa: str, session: Session = Depends(get_session)):
    return MesasService(session).obtener(idmesa)

@router.put("/{idmesa}", response_model=MesaRead)
def actualizar_mesa(idmesa: str, payload: MesaCreate, session: Session = Depends(get_session)):
    return MesasService(session).actualizar(idmesa, payload)

@router.delete("/{idmesa}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mesa(idmesa: str, session: Session = Depends(get_session)):
    MesasService(session).eliminar(idmesa)
    return None
