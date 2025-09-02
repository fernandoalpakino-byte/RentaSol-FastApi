from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.database.database import get_session
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(payload: LoginRequest, session: Session = Depends(get_session)):
    return AuthService(session).login(payload)
