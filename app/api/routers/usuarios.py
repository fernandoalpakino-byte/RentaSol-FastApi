from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.database.database import get_session
from app.schemas.usuarios import UsuarioCreate, UsuarioRead, UsuarioUpdate
from app.services.usuarios_service import UsuariosService

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
def crear_usuario(payload: UsuarioCreate, session: Session = Depends(get_session)):
    return UsuariosService(session).crear(payload)

@router.get("", response_model=List[UsuarioRead])
def listar_usuarios(session: Session = Depends(get_session)):
    return UsuariosService(session).listar()

@router.get("/{idusuario}", response_model=UsuarioRead)
def obtener_usuario(idusuario: str, session: Session = Depends(get_session)):
    return UsuariosService(session).obtener(idusuario)

@router.patch("/{idusuario}", response_model=UsuarioRead)
def actualizar_usuario(idusuario: str, payload: UsuarioUpdate, session: Session = Depends(get_session)):
    return UsuariosService(session).actualizar(idusuario, payload)

@router.delete("/{idusuario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(idusuario: str, session: Session = Depends(get_session)):
    UsuariosService(session).eliminar(idusuario)
    return None
