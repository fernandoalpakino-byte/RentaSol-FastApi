from fastapi import HTTPException
from sqlmodel import Session
from app.models import Usuario
from app.schemas.usuarios import UsuarioCreate, UsuarioRead, UsuarioUpdate
from app.repositories.usuarios_repository import UsuariosRepository
from datetime import datetime

class UsuariosService:
    def __init__(self, session: Session):
        self.repo = UsuariosRepository(session)

    def crear(self, payload: UsuarioCreate) -> UsuarioRead:
        usuario = Usuario(
            nombre=payload.nombre,
            apellido=payload.apellido,
            ruc=payload.ruc,
            correo=payload.correo,
            telefono=payload.telefono,
            password=payload.password,  # TODO: hash
            tipousuario=payload.tipousuario,
        )
        usuario = self.repo.crear(usuario)
        return UsuarioRead(
            idusuario=usuario.idusuario,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            ruc=usuario.ruc,
            correo=usuario.correo,
            telefono=usuario.telefono,
            tipousuario=usuario.tipousuario,
            fechacreacion=usuario.fechacreacion,
        )

    def listar(self):
        usuarios = self.repo.obtener_todos()
        return [
            UsuarioRead(
                idusuario=u.idusuario,
                nombre=u.nombre,
                apellido=u.apellido,
                ruc=u.ruc,
                correo=u.correo,
                telefono=u.telefono,
                tipousuario=u.tipousuario,
                fechacreacion=u.fechacreacion,
            )
            for u in usuarios
        ]

    def obtener(self, idusuario: str) -> UsuarioRead:
        usuario = self.repo.obtener_por_id(idusuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return UsuarioRead(
            idusuario=usuario.idusuario,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            ruc=usuario.ruc,
            correo=usuario.correo,
            telefono=usuario.telefono,
            tipousuario=usuario.tipousuario,
            fechacreacion=usuario.fechacreacion,
        )

    def actualizar(self, idusuario: str, payload: UsuarioUpdate) -> UsuarioRead:
        usuario = self.repo.obtener_por_id(idusuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(usuario, k, v)
        usuario = self.repo.actualizar(usuario)
        return self.obtener(idusuario)

    def eliminar(self, idusuario: str) -> None:
        usuario = self.repo.obtener_por_id(idusuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        self.repo.eliminar(usuario)
