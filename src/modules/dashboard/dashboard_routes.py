from fastapi import APIRouter, Depends, Query
from src.core.middleware.auth import get_current_user
from src.modules.dashboard import dashboard_controller as controller

router = APIRouter(prefix="/Dashboard", tags=["Dashboard"], dependencies=[Depends(get_current_user)])
reports_router = APIRouter(prefix="/Reports", tags=["Reports"], dependencies=[Depends(get_current_user)])

@router.get('/fetchanomalycameras', name='API_GET_ACAMERAS')
async def get_acameras(PageNumber:int=Query(1), PageSize:int=Query(1000)):
    return await controller.handle('API_GET_ACAMERAS', f'/fetchanomalycameras?PageNumber={PageNumber}&PageSize={PageSize}', True)

@router.get('/fetchunitsall', name='API_GET_UNITS')
async def get_units(PageNumber:int=Query(1), PageSize:int=Query(1000)):
    return await controller.handle('API_GET_UNITS', f'/fetchunitsall?PageNumber={PageNumber}&PageSize={PageSize}', True)

@router.get('/fetchusertab', name='API_GET_USERTAB')
async def get_user_tab():
    return await controller.handle('API_GET_USERTAB', '/fetchusertab', True)

@router.post('/createusertab', name='API_CREATE_USER_TAB')
async def create_user_tab():
    return await controller.handle('API_CREATE_USER_TAB', '/createusertab', False)

@router.delete('/deleteusertab/{tab_id}', name='API_DELETE_TAB')
async def delete_user_tab(tab_id:str):
    return await controller.handle('API_DELETE_TAB', f'/deleteusertab/{tab_id}', False)

@reports_router.get('/fetchnotificationbydate', name='API_FETCH_NOTIFICATION_BY_DATE')
async def fetch_date(): return await controller.handle('API_FETCH_NOTIFICATION_BY_DATE','/fetchnotificationbydate',True)
@reports_router.get('/fetchnoticiationvehicle', name='API_FETCH_NOTIFICATION_BY_VEHICLE')
async def fetch_vehicle(): return await controller.handle('API_FETCH_NOTIFICATION_BY_VEHICLE','/fetchnoticiationvehicle',True)
@reports_router.get('/fetchnoticiationface', name='API_FETCH_NOTIFICATION_BY_FACE')
async def fetch_face(): return await controller.handle('API_FETCH_NOTIFICATION_BY_FACE','/fetchnoticiationface',True)
