from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from typing import Optional, Dict, Any
from app.core.config import settings

def create_access_token(subject: str, extra_claims: Optional[Dict[str, Any]] = None, expires_minutes: Optional[int] = None) -> str:
    expire_minutes = expires_minutes or settings.jwt.access_token_expire_minutes
    to_encode = {
        "sub": subject,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expire_minutes),
        "iat": datetime.now(timezone.utc),
    }
    if extra_claims:
        to_encode.update(extra_claims)
    return jwt.encode(to_encode, settings.jwt.secret_key, algorithm=settings.jwt.algorithm)

def decode_access_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.jwt.secret_key, algorithms=[settings.jwt.algorithm])
        return payload
    except JWTError as e:
        raise ValueError("Token inválido o expirado") from e
