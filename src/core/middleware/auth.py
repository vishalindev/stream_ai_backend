from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.core.config.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

FAKE_USERS = {
    "admin": {
        "username": "admin",
        "full_name": "Platform Admin",
        "hashed_password": pwd_context.hash("admin123"),
        "disabled": False,
    }
}


def authenticate_user(username: str, password: str):
    user = FAKE_USERS.get(username)
    if user and pwd_context.verify(password, user["hashed_password"]):
        return user
    return None


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({"sub": subject, "exp": expire}, settings.secret_key, algorithm=settings.algorithm)


def get_current_user(token: str = Depends(oauth2_scheme)):
    error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError as exc:
        raise error from exc
    user = FAKE_USERS.get(payload.get("sub"))
    if not user or user.get("disabled"):
        raise error
    return user
