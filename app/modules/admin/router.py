from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.modules.admin.schemas import DomainPayload
from app.modules.admin.service import employee_service, plant_service

employee_router = APIRouter(prefix="/Employee", tags=["Employee Management"], dependencies=[Depends(get_current_user)])
plant_router = APIRouter(prefix="/Plant", tags=["Plant Infrastructure Setup"], dependencies=[Depends(get_current_user)])


@employee_router.post("/createuser", name="API_SAVE_EMPLOYEE")
async def save_employee(payload: DomainPayload):
    return await employee_service.execute("API_SAVE_EMPLOYEE", "/createuser", action="create", payload=payload.model_dump())


@employee_router.put("/updateuser", name="API_UPDATE_EMPLOYEE")
async def update_employee(payload: DomainPayload):
    return await employee_service.execute("API_UPDATE_EMPLOYEE", "/updateuser", action="update", payload=payload.model_dump())


@employee_router.get("/fetchusers", name="API_GET_EMPLOYEES")
async def get_employees(PageNumber: int = Query(1, ge=1), PageSize: int = Query(100, ge=1, le=5000)):
    return await employee_service.execute("API_GET_EMPLOYEES", f"/fetchusers?PageNumber={PageNumber}&PageSize={PageSize}", action="list")


@plant_router.post("/createplant", name="API_SAVE_PLANTSETUP")
async def save_plant(payload: DomainPayload):
    return await plant_service.execute("API_SAVE_PLANTSETUP", "/createplant", action="create", payload=payload.model_dump())


@plant_router.put("/updateplant", name="API_UPDATE_PLANTSETUP")
async def update_plant(payload: DomainPayload):
    return await plant_service.execute("API_UPDATE_PLANTSETUP", "/updateplant", action="update", payload=payload.model_dump())


@plant_router.get("/fetchplant", name="API_GET_PLANTSETUPS")
async def get_plants(PageNumber: int = Query(1, ge=1), PageSize: int = Query(100, ge=1, le=5000)):
    return await plant_service.execute("API_GET_PLANTSETUPS", f"/fetchplant?PageNumber={PageNumber}&PageSize={PageSize}", action="list")
