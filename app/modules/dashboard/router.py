from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.shared.schemas.common import DomainPayload
from app.modules.dashboard.service import service

router = APIRouter(prefix="/Dashboard", tags=["Live Dashboard & Workspaces"], dependencies=[Depends(get_current_user)])


@router.get("/fetchanomalycameras", name="API_GET_ACAMERAS")
async def get_anomaly_cameras(PageNumber: int = Query(1, ge=1), PageSize: int = Query(1000, ge=1, le=5000)):
    return await service.execute("API_GET_ACAMERAS", f"/fetchanomalycameras?PageNumber={PageNumber}&PageSize={PageSize}")


@router.get("/fetchunitsall", name="API_GET_UNITS")
async def get_units(PageNumber: int = Query(1, ge=1), PageSize: int = Query(1000, ge=1, le=5000)):
    return await service.execute("API_GET_UNITS", f"/fetchunitsall?PageNumber={PageNumber}&PageSize={PageSize}")


@router.get("/fetchusertab", name="API_GET_USERTAB")
async def get_user_tab():
    return await service.execute("API_GET_USERTAB", "/fetchusertab")


@router.post("/createusertab", name="API_CREATE_USER_TAB")
async def create_user_tab(payload: DomainPayload):
    return await service.execute("API_CREATE_USER_TAB", "/createusertab", action="create", payload=payload.model_dump())


@router.get("/fetchusertab", name="API_FETCH_USER_TAB")
async def fetch_user_tab():
    return await service.execute("API_FETCH_USER_TAB", "/fetchusertab")


@router.delete("/deleteusertab/", name="API_DELETE_TAB")
async def delete_tab(tab_id: str | None = Query(None)):
    path = f"/deleteusertab/?tab_id={tab_id}" if tab_id else "/deleteusertab/"
    return await service.execute("API_DELETE_TAB", path, action="update", payload={"tab_id": tab_id, "deleted": True})
