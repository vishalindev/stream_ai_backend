from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.modules.reports.service import service

router = APIRouter(prefix="/Reports", tags=["Analytical Reports"], dependencies=[Depends(get_current_user)])


@router.get("/fetchnotificationbydate", name="API_FETCH_NOTIFICATION_BY_DATE")
async def fetch_notification_by_date():
    return await service.execute("API_FETCH_NOTIFICATION_BY_DATE", "/fetchnotificationbydate")


@router.get("/fetchnoticiationvehicle", name="API_FETCH_NOTIFICATION_BY_VEHICLE")
async def fetch_notification_by_vehicle():
    return await service.execute("API_FETCH_NOTIFICATION_BY_VEHICLE", "/fetchnoticiationvehicle")


@router.get("/fetchnoticiationface", name="API_FETCH_NOTIFICATION_BY_FACE")
async def fetch_notification_by_face():
    return await service.execute("API_FETCH_NOTIFICATION_BY_FACE", "/fetchnoticiationface")
