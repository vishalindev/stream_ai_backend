from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.shared.schemas.common import DomainPayload
from app.modules.camera.service import service

router = APIRouter(prefix="/Camera", tags=["Camera & Video Assets"], dependencies=[Depends(get_current_user)])


@router.post("/addcamera", name="API_SAVE_CAMERA")
async def save_camera(payload: DomainPayload):
    return await service.execute("API_SAVE_CAMERA", "/addcamera", action="create", payload=payload.model_dump())


@router.put("/updatecamera", name="API_UPDATE_CAMERA")
async def update_camera(payload: DomainPayload):
    return await service.execute("API_UPDATE_CAMERA", "/updatecamera", action="update", payload=payload.model_dump())


@router.get("/fetchcamerasall", name="API_GET_CAMERAS")
async def get_cameras(PageNumber: int = Query(1, ge=1), PageSize: int = Query(100, ge=1, le=5000)):
    return await service.execute("API_GET_CAMERAS", f"/fetchcamerasall?PageNumber={PageNumber}&PageSize={PageSize}", action="list")


@router.get("/departmentwithcamera", name="API_GET_CAMERA_UNITS")
async def get_camera_units():
    return await service.execute("API_GET_CAMERA_UNITS", "/departmentwithcamera")
