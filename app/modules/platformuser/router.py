from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.shared.schemas.common import DomainPayload
from app.modules.platformuser.service import service

router = APIRouter(prefix="/PlatFormUser", tags=["Platform User & RBAC Administration"], dependencies=[Depends(get_current_user)])


@router.post("", name="API_SAVE_PLATFORMUSER")
async def save_platform_user(payload: DomainPayload):
    return await service.execute("API_SAVE_PLATFORMUSER", "/PlatFormUser", action="create", payload=payload.model_dump())


@router.put("/updateplatformuser", name="API_UPDATE_PLATFORMUSER")
async def update_platform_user(payload: DomainPayload):
    return await service.execute("API_UPDATE_PLATFORMUSER", "/updateplatformuser", action="update", payload=payload.model_dump())


@router.get("/fetchallplatformusers", name="API_GET_PLATFORMUSERS")
async def get_platform_users(PageNumber: int = Query(1, ge=1), PageSize: int = Query(1000, ge=1, le=5000)):
    return await service.execute("API_GET_PLATFORMUSERS", f"/fetchallplatformusers?PageNumber={PageNumber}&PageSize={PageSize}", action="list")


@router.get("/fetchroleall", name="API_GET_ROLES")
async def get_roles(PageNumber: int = Query(1, ge=1), PageSize: int = Query(100, ge=1, le=5000)):
    return await service.execute("API_GET_ROLES", f"/fetchroleall?PageNumber={PageNumber}&PageSize={PageSize}")


@router.get("/fetchdesignationall", name="API_GET_DESIGNATIONS")
async def get_designations():
    return await service.execute("API_GET_DESIGNATIONS", "/fetchdesignationall")
