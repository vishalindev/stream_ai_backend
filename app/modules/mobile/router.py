from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.modules.mobile.service import service

router = APIRouter(prefix="/Mobile", tags=["Mobile"], dependencies=[Depends(get_current_user)])


@router.get("/health", name="API_MOBILE_HEALTH")
async def mobile_health():
    return await service.execute("API_MOBILE_HEALTH", "/health", use_cache=False)
