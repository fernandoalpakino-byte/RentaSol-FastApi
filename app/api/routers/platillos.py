from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.database.database import get_session
from app.schemas.platillos import PlatilloCreate, PlatilloRead
from app.services.platillos_service import PlatillosService
from app.api.deps.authz import require_roles

router = APIRouter(prefix="/platillos", tags=["platillos"])

@router.post("", response_model=PlatilloRead, status_code=status.HTTP_201_CREATED)
def crear_platillo(payload: PlatilloCreate, session: Session = Depends(get_session), current_user=Depends(require_roles("Admin"))):
    return PlatillosService(session).crear(payload)

@router.get("", response_model=List[PlatilloRead])
def listar_platillos(session: Session = Depends(get_session), current_user=Depends(require_roles("Admin"))):
    return PlatillosService(session).listar()

@router.get("/{idplatillo}", response_model=PlatilloRead)
def obtener_platillo(idplatillo: str, session: Session = Depends(get_session), current_user=Depends(require_roles("Admin"))):
    return PlatillosService(session).obtener(idplatillo)

@router.put("/{idplatillo}", response_model=PlatilloRead)
def actualizar_platillo(idplatillo: str, payload: PlatilloCreate, session: Session = Depends(get_session), current_user=Depends(require_roles("admin"))):
    return PlatillosService(session).actualizar(idplatillo, payload)

@router.delete("/{idplatillo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_platillo(idplatillo: str, session: Session = Depends(get_session), current_user=Depends(require_roles("Admin"))):
    PlatillosService(session).eliminar(idplatillo)
    return None
