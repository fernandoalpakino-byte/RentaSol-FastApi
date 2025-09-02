from fastapi import HTTPException
from sqlmodel import Session
from app.repositories.usuarios_repository import UsuariosRepository
from app.utils.security import verify_password
from app.utils.jwt import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse

class AuthService:
    def __init__(self, session: Session):
        self.users = UsuariosRepository(session)

    def login(self, payload: LoginRequest) -> TokenResponse:
        user = self.users.obtener_por_correo(payload.correo)
        if not user or not verify_password(payload.password, user.password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        token = create_access_token(subject=user.idusuario, extra_claims={
            "correo": user.correo,
            "tipousuario": user.tipousuario,
        })
        return TokenResponse(access_token=token)
