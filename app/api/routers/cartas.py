from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.database.database import get_session
from app.schemas.cartas import CartaCreate, CartaRead
from app.services.cartas_service import CartasService

router = APIRouter(prefix="/cartas", tags=["cartas"])

@router.post("", response_model=CartaRead, status_code=status.HTTP_201_CREATED)
def crear_carta(payload: CartaCreate, session: Session = Depends(get_session)):
    return CartasService(session).crear(payload)

@router.get("", response_model=List[CartaRead])
def listar_cartas(session: Session = Depends(get_session)):
    return CartasService(session).listar()

@router.get("/{idcarta}", response_model=CartaRead)
def obtener_carta(idcarta: str, session: Session = Depends(get_session)):
    return CartasService(session).obtener(idcarta)

@router.put("/{idcarta}", response_model=CartaRead)
def actualizar_carta(idcarta: str, payload: CartaCreate, session: Session = Depends(get_session)):
    return CartasService(session).actualizar(idcarta, payload)

@router.delete("/{idcarta}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_carta(idcarta: str, session: Session = Depends(get_session)):
    CartasService(session).eliminar(idcarta)
    return None
