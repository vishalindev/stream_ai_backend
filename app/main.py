from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.core.auth import authenticate_user, create_access_token
from app.core.cache import close_redis, init_redis
from app.core.config import settings
from app.routers.common import build_router

limiter = Limiter(key_func=get_remote_address, default_limits=[settings.default_rate_limit])

app = FastAPI(title=settings.app_name)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.on_event("startup")
async def startup() -> None:
    await init_redis()


@app.on_event("shutdown")
async def shutdown() -> None:
    await close_redis()


@app.post("/auth/token", tags=["Auth"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return {"error": "invalid_credentials"}
    return {"access_token": create_access_token({"sub": user["username"]}), "token_type": "bearer"}


dashboard_endpoints = [
    ("API_GET_ACAMERAS", "GET", "/fetchanomalycameras"),
    ("API_GET_UNITS", "GET", "/fetchunitsall"),
    ("API_GET_USERTAB", "GET", "/fetchusertab"),
    ("API_CREATE_USER_TAB", "POST", "/createusertab"),
    ("API_DELETE_TAB", "DELETE", "/deleteusertab/{tab_id}"),
]
camera_endpoints = [
    ("API_SAVE_CAMERA", "POST", "/addcamera"),
    ("API_UPDATE_CAMERA", "PUT", "/updatecamera"),
    ("API_GET_CAMERAS", "GET", "/fetchcamerasall"),
    ("API_GET_CAMERA_UNITS", "GET", "/departmentwithcamera"),
]
zone_endpoints = [
    ("API_UPDATE_ZONE", "PUT", "/updatezone"),
    ("API_GET_ZONES", "GET", "/fetchzoneall"),
    ("API_GET_CAMERABYZONEID", "GET", "/fetchzonebyid"),
    ("API_GET_ZONE_CODE", "GET", "/createzonecode"),
    ("API_UPDATE_ZONE_CAMERA", "PUT", "/zonecameramap"),
    ("API_UPDATE_ZONE_RULE", "PUT", "/zonerulemap"),
    ("API_GET_ZONE_USER_TAB", "GET", "/fetchzonebytabid"),
]
notification_endpoints = [
    ("API_GET_NOTIFICATIONSBYCAMERAID", "GET", "/fetchnotificationbycameraid"),
    ("API_GET_NOTIFICATIONBYID", "GET", "/fetchnotificationbyid"),
    ("API_GET_NOTIFICATIONARRAY", "GET", "/getnotificationarray"),
    ("API_GET_TODAYSNOTIFICATIONS", "GET", "/fetchnotification"),
    ("API_POST_NOTIFICATION_STATUS", "POST", "/notificationstatusupdate"),
]
notification_group_endpoints = [
    ("API_SAVE_NOTIFICATIONGROUP", "POST", "/addnotificationgroup"),
    ("API_UPDATE_NOTIFICATIONGROUP", "PUT", "/updatenotificationgroup"),
    ("API_GET_NOTIFICATIONGROUPS", "GET", "/fetchnotificationgroupall"),
]
rule_endpoints = [
    ("API_SAVE_RULE", "POST", "/addnotificationrule"),
    ("API_UPDATE_RULE", "PUT", "/updaterule"),
    ("API_GET_RULES", "GET", "/fetchruleall"),
    ("API_GET_RULEBYUNITID", "GET", "/fetchrulebyunitid"),
]
reports_endpoints = [
    ("API_FETCH_NOTIFICATION_BY_DATE", "GET", "/fetchnotificationbydate"),
    ("API_FETCH_NOTIFICATION_BY_VEHICLE", "GET", "/fetchnoticiationvehicle"),
    ("API_FETCH_NOTIFICATION_BY_FACE", "GET", "/fetchnoticiationface"),
]
platform_user_endpoints = [
    ("API_SAVE_PLATFORMUSER", "POST", "/"),
    ("API_UPDATE_PLATFORMUSER", "PUT", "/updateplatformuser"),
    ("API_GET_PLATFORMUSERS", "GET", "/fetchallplatformusers"),
    ("API_GET_ROLES", "GET", "/fetchroleall"),
    ("API_GET_DESIGNATIONS", "GET", "/fetchdesignationall"),
]
plant_endpoints = [
    ("API_SAVE_PLANTSETUP", "POST", "/createplant"),
    ("API_UPDATE_PLANTSETUP", "PUT", "/updateplant"),
    ("API_GET_PLANTSETUPS", "GET", "/fetchplant"),
]
employee_endpoints = [
    ("API_SAVE_EMPLOYEE", "POST", "/createuser"),
    ("API_UPDATE_EMPLOYEE", "PUT", "/updateuser"),
    ("API_GET_EMPLOYEES", "GET", "/fetchusers"),
]
external_endpoints = [
    ("API_GET_ACCESSROLES", "GET", "/fetchuserroleall"),
    ("API_VIEW_WIP", "GET", "/viewwip"),
    ("API_GET_PRESIGNED_URL", "GET", "/s3upload"),
]

for tag, endpoints in [
    ("Dashboard", dashboard_endpoints),
    ("Camera", camera_endpoints),
    ("Zone", zone_endpoints),
    ("Notification", notification_endpoints),
    ("NotificationGroup", notification_group_endpoints),
    ("Rule", rule_endpoints),
    ("Reports", reports_endpoints),
    ("PlatFormUser", platform_user_endpoints),
    ("Plant", plant_endpoints),
    ("Employee", employee_endpoints),
    ("External", external_endpoints),
]:
    app.include_router(build_router(tag, endpoints))
