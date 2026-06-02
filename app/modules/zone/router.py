from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.shared.schemas.common import DomainPayload
from app.modules.zone.service import service

router = APIRouter(prefix="/Zone", tags=["Zones & Area Mapping"], dependencies=[Depends(get_current_user)])


@router.post("/createzone", name="API_SAVE_ZONE")
async def save_zone(payload: DomainPayload):
    return await service.execute("API_SAVE_ZONE", "/createzone", action="create", payload=payload.model_dump())


@router.put("/updatezone", name="API_UPDATE_ZONE")
async def update_zone(payload: DomainPayload):
    return await service.execute("API_UPDATE_ZONE", "/updatezone", action="update", payload=payload.model_dump())


@router.get("/fetchzoneall", name="API_GET_ZONES")
async def get_zones(PageNumber: int = Query(1, ge=1), PageSize: int = Query(100, ge=1, le=5000)):
    return await service.execute("API_GET_ZONES", f"/fetchzoneall?PageNumber={PageNumber}&PageSize={PageSize}", action="list")


@router.get("/fetchzonebyid", name="API_GET_CAMERABYZONEID")
async def get_camera_by_zone_id(zone_id: str = Query(...)):
    return await service.execute("API_GET_CAMERABYZONEID", f"/fetchzonebyid?zone_id={zone_id}")


@router.get("/createzonecode", name="API_GET_ZONE_CODE")
async def get_zone_code():
    return await service.execute("API_GET_ZONE_CODE", "/createzonecode")


@router.put("/zonecameramap", name="API_UPDATE_ZONE_CAMERA")
async def update_zone_camera(payload: DomainPayload):
    return await service.execute("API_UPDATE_ZONE_CAMERA", "/zonecameramap", action="update", payload=payload.model_dump())


@router.put("/zonerulemap", name="API_UPDATE_ZONE_RULE")
async def update_zone_rule(payload: DomainPayload):
    return await service.execute("API_UPDATE_ZONE_RULE", "/zonerulemap", action="update", payload=payload.model_dump())


@router.get("/fetchzonebytabid", name="API_GET_ZONE_USER_TAB")
async def get_zone_user_tab(tab_id: str = Query(...)):
    return await service.execute("API_GET_ZONE_USER_TAB", f"/fetchzonebytabid?tab_id={tab_id}")
