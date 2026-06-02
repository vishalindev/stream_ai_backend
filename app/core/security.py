from datetime import datetime, timedelta, timezone
from hashlib import sha256
from hmac import compare_digest

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def _hash_password(password: str) -> str:
    return sha256(password.encode("utf-8")).hexdigest()


FAKE_USERS = {
    "admin": {
        "username": "admin",
        "full_name": "Platform Admin",
        "hashed_password": _hash_password("admin123"),
        "disabled": False,
    }
}


def authenticate_user(username: str, password: str):
    user = FAKE_USERS.get(username)
    if user and compare_digest(user["hashed_password"], _hash_password(password)):
        return user
    return None


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({"sub": subject, "exp": expire}, settings.secret_key, algorithm=settings.algorithm)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError as exc:
        raise credentials_error from exc
    user = FAKE_USERS.get(payload.get("sub"))
    if not user or user.get("disabled"):
        raise credentials_error
    return user
