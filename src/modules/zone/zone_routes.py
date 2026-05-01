from fastapi import APIRouter, Depends, Query
from src.core.middleware.auth import get_current_user
from src.modules.zone import zone_controller as controller
router = APIRouter(prefix="/Zone", tags=["Zone"], dependencies=[Depends(get_current_user)])
plant_router = APIRouter(prefix="/Plant", tags=["Plant"], dependencies=[Depends(get_current_user)])

@router.put('/updatezone', name='API_UPDATE_ZONE')
async def update_zone(): return await controller.handle('API_UPDATE_ZONE','/updatezone',False)
@router.get('/fetchzoneall', name='API_GET_ZONES')
async def fetch_zone(PageNumber:int=Query(1),PageSize:int=Query(100)): return await controller.handle('API_GET_ZONES',f'/fetchzoneall?PageNumber={PageNumber}&PageSize={PageSize}',True)
@router.get('/fetchzonebyid', name='API_GET_CAMERABYZONEID')
async def fetch_by_id(zone_id:str=Query(...)): return await controller.handle('API_GET_CAMERABYZONEID',f'/fetchzonebyid?zone_id={zone_id}',True)
@router.get('/createzonecode', name='API_GET_ZONE_CODE')
async def zone_code(): return await controller.handle('API_GET_ZONE_CODE','/createzonecode',True)
@router.put('/zonecameramap', name='API_UPDATE_ZONE_CAMERA')
async def zone_camera(): return await controller.handle('API_UPDATE_ZONE_CAMERA','/zonecameramap',False)
@router.put('/zonerulemap', name='API_UPDATE_ZONE_RULE')
async def zone_rule(): return await controller.handle('API_UPDATE_ZONE_RULE','/zonerulemap',False)
@router.get('/fetchzonebytabid', name='API_GET_ZONE_USER_TAB')
async def zone_tab(tab_id:str=Query(...)): return await controller.handle('API_GET_ZONE_USER_TAB',f'/fetchzonebytabid?tab_id={tab_id}',True)

@plant_router.post('/createplant', name='API_SAVE_PLANTSETUP')
async def create_plant(): return await controller.handle('API_SAVE_PLANTSETUP','/createplant',False)
@plant_router.put('/updateplant', name='API_UPDATE_PLANTSETUP')
async def update_plant(): return await controller.handle('API_UPDATE_PLANTSETUP','/updateplant',False)
@plant_router.get('/fetchplant', name='API_GET_PLANTSETUPS')
async def get_plant(PageNumber:int=Query(1),PageSize:int=Query(100)): return await controller.handle('API_GET_PLANTSETUPS',f'/fetchplant?PageNumber={PageNumber}&PageSize={PageSize}',True)
