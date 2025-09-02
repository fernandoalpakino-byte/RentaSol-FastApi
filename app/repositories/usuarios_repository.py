from typing import Optional, List
from sqlmodel import Session, select
from app.models import Usuario

class UsuariosRepository:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def obtener_todos(self) -> List[Usuario]:
        return self.session.exec(select(Usuario)).all()

    def obtener_por_id(self, idusuario: str) -> Optional[Usuario]:
        return self.session.get(Usuario, idusuario)

    def actualizar(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def eliminar(self, usuario: Usuario) -> None:
        self.session.delete(usuario)
        self.session.commit()
