from fastapi import APIRouter, Depends
from src.core.middleware.auth import get_current_user
from src.modules.dashboard import dashboard_controller as controller

router = APIRouter(prefix="/Dashboard", tags=["Dashboard"], dependencies=[Depends(get_current_user)])

ENDPOINTS = [
    ("API_GET_ACAMERAS", "GET", "/fetchanomalycameras", True),
    ("API_GET_UNITS", "GET", "/fetchunitsall", True),
    ("API_GET_USERTAB", "GET", "/fetchusertab", True),
    ("API_CREATE_USER_TAB", "POST", "/createusertab", False),
    ("API_DELETE_TAB", "DELETE", "/deleteusertab/{tab_id}", False),
    ("API_FETCH_NOTIFICATION_BY_DATE", "GET", "/fetchnotificationbydate", True),
    ("API_FETCH_NOTIFICATION_BY_VEHICLE", "GET", "/fetchnoticiationvehicle", True),
    ("API_FETCH_NOTIFICATION_BY_FACE", "GET", "/fetchnoticiationface", True),
]
for name, method, path, use_cache in ENDPOINTS:
    async def handler(_name=name, _path=path, _cache=use_cache):
        return await controller.handle(_name, _path, _cache)
    getattr(router, method.lower())(path, name=name)(handler)
