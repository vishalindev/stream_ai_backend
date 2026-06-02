from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.shared.schemas.common import DomainPayload
from app.modules.notification.service import service

notification_router = APIRouter(prefix="/Notification", tags=["Real-time Notifications"], dependencies=[Depends(get_current_user)])
notification_group_router = APIRouter(prefix="/NotificationGroup", tags=["Notification Grouping"], dependencies=[Depends(get_current_user)])


@notification_group_router.post("/addnotificationgroup", name="API_SAVE_NOTIFICATIONGROUP")
async def save_notification_group(payload: DomainPayload):
    return await service.execute("API_SAVE_NOTIFICATIONGROUP", "/addnotificationgroup", action="create", payload=payload.model_dump())


@notification_group_router.put("/updatenotificationgroup", name="API_UPDATE_NOTIFICATIONGROUP")
async def update_notification_group(payload: DomainPayload):
    return await service.execute("API_UPDATE_NOTIFICATIONGROUP", "/updatenotificationgroup", action="update", payload=payload.model_dump())


@notification_group_router.get("/fetchnotificationgroupall", name="API_GET_NOTIFICATIONGROUPS")
async def get_notification_groups(PageNumber: int = Query(1, ge=1), PageSize: int = Query(1000, ge=1, le=5000)):
    return await service.execute("API_GET_NOTIFICATIONGROUPS", f"/fetchnotificationgroupall?PageNumber={PageNumber}&PageSize={PageSize}", action="list")


@notification_router.get("/fetchnotificationbycameraid", name="API_GET_NOTIFICATIONSBYCAMERAID")
async def get_notifications_by_camera_id(camera_id: str | None = Query(None)):
    path = f"/fetchnotificationbycameraid?camera_id={camera_id}" if camera_id else "/fetchnotificationbycameraid"
    return await service.execute("API_GET_NOTIFICATIONSBYCAMERAID", path)


@notification_router.get("/fetchnotificationbyid", name="API_GET_NOTIFICATIONBYID")
async def get_notification_by_id(notification_id: str | None = Query(None)):
    path = f"/fetchnotificationbyid?notification_id={notification_id}" if notification_id else "/fetchnotificationbyid"
    return await service.execute("API_GET_NOTIFICATIONBYID", path)


@notification_router.get("/getnotificationarray", name="API_GET_NOTIFICATIONARRAY")
async def get_notification_array():
    return await service.execute("API_GET_NOTIFICATIONARRAY", "/getnotificationarray")


@notification_router.get("/fetchnotification", name="API_GET_TODAYSNOTIFICATIONS")
async def get_todays_notifications():
    return await service.execute("API_GET_TODAYSNOTIFICATIONS", "/fetchnotification")


@notification_router.post("/notificationstatusupdate", name="API_POST_NOTIFICATION_STATUS")
async def update_notification_status(payload: DomainPayload):
    return await service.execute("API_POST_NOTIFICATION_STATUS", "/notificationstatusupdate", action="update", payload=payload.model_dump())
