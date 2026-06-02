from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.modules.identity.auth import authenticate_user, create_access_token

router = APIRouter(tags=["Auth"])


@router.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return {"error": "invalid_credentials"}
    return {"access_token": create_access_token(user["username"]), "token_type": "bearer"}
