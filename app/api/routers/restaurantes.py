from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.database.database import get_session
from app.schemas.restaurantes import RestauranteCreate, RestauranteRead
from app.services.restaurantes_service import RestaurantesService

router = APIRouter(prefix="/restaurantes", tags=["restaurantes"])

@router.post("", response_model=RestauranteRead, status_code=status.HTTP_201_CREATED)
def crear_restaurante(payload: RestauranteCreate, session: Session = Depends(get_session)):
    return RestaurantesService(session).crear(payload)

@router.get("", response_model=List[RestauranteRead])
def listar_restaurantes(session: Session = Depends(get_session)):
    return RestaurantesService(session).listar()

@router.get("/{idrestaurante}", response_model=RestauranteRead)
def obtener_restaurante(idrestaurante: str, session: Session = Depends(get_session)):
    return RestaurantesService(session).obtener(idrestaurante)

@router.put("/{idrestaurante}", response_model=RestauranteRead)
def actualizar_restaurante(idrestaurante: str, payload: RestauranteCreate, session: Session = Depends(get_session)):
    return RestaurantesService(session).actualizar(idrestaurante, payload)

@router.delete("/{idrestaurante}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_restaurante(idrestaurante: str, session: Session = Depends(get_session)):
    RestaurantesService(session).eliminar(idrestaurante)
    return None
