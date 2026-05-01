from fastapi import APIRouter, Depends
from src.core.middleware.auth import get_current_user
from src.modules.camera import camera_controller as controller
router = APIRouter(prefix="/Camera", tags=["Camera"], dependencies=[Depends(get_current_user)])
ENDPOINTS=[("API_SAVE_CAMERA","POST","/addcamera",False),("API_UPDATE_CAMERA","PUT","/updatecamera",False),("API_GET_CAMERAS","GET","/fetchcamerasall",True),("API_GET_CAMERA_UNITS","GET","/departmentwithcamera",True)]
for n,m,p,c in ENDPOINTS:
    async def h(_n=n,_p=p,_c=c): return await controller.handle(_n,_p,_c)
    getattr(router,m.lower())(p,name=n)(h)
