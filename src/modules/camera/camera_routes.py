from fastapi import APIRouter, Depends, Query
from src.core.middleware.auth import get_current_user
from src.modules.camera import camera_controller as controller
router = APIRouter(prefix="/Camera", tags=["Camera"], dependencies=[Depends(get_current_user)])

@router.post('/addcamera', name='API_SAVE_CAMERA')
async def save_camera(): return await controller.handle('API_SAVE_CAMERA','/addcamera',False)
@router.put('/updatecamera', name='API_UPDATE_CAMERA')
async def update_camera(): return await controller.handle('API_UPDATE_CAMERA','/updatecamera',False)
@router.get('/fetchcamerasall', name='API_GET_CAMERAS')
async def get_cameras(PageNumber:int=Query(1),PageSize:int=Query(100)): return await controller.handle('API_GET_CAMERAS',f'/fetchcamerasall?PageNumber={PageNumber}&PageSize={PageSize}',True)
@router.get('/departmentwithcamera', name='API_GET_CAMERA_UNITS')
async def get_units(): return await controller.handle('API_GET_CAMERA_UNITS','/departmentwithcamera',True)
