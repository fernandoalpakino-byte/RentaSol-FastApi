from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from datetime import datetime

from app.database.database import get_session
from app.schemas.reservas import ReservaCreate, ReservaRead
from app.services.reservas_service import ReservasService
from app.api.deps.authz import get_current_user

router = APIRouter(prefix="/restaurantes/{idrestaurante}/reservas", tags=["reservas"])

@router.post("", response_model=ReservaRead, status_code=status.HTTP_201_CREATED)
def crear_reserva(idrestaurante: str, payload: ReservaCreate, session: Session = Depends(get_session), current_user = Depends(get_current_user)):
    service = ReservasService(session)
    return service.crear_reserva(idrestaurante, payload)
