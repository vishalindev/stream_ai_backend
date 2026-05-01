from fastapi import APIRouter, Depends
from src.core.middleware.auth import get_current_user
from src.modules.zone import zone_controller as controller
router = APIRouter(prefix="/Zone", tags=["Zone"], dependencies=[Depends(get_current_user)])
ENDPOINTS=[("API_UPDATE_ZONE","PUT","/updatezone",False),("API_GET_ZONES","GET","/fetchzoneall",True),("API_GET_CAMERABYZONEID","GET","/fetchzonebyid",True),("API_GET_ZONE_CODE","GET","/createzonecode",True),("API_UPDATE_ZONE_CAMERA","PUT","/zonecameramap",False),("API_UPDATE_ZONE_RULE","PUT","/zonerulemap",False),("API_GET_ZONE_USER_TAB","GET","/fetchzonebytabid",True),("API_SAVE_PLANTSETUP","POST","/createplant",False),("API_UPDATE_PLANTSETUP","PUT","/updateplant",False),("API_GET_PLANTSETUPS","GET","/fetchplant",True)]
for n,m,p,c in ENDPOINTS:
    async def h(_n=n,_p=p,_c=c): return await controller.handle(_n,_p,_c)
    getattr(router,m.lower())(p,name=n)(h)
