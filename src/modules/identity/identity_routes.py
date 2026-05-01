from fastapi import APIRouter, Depends
from src.core.middleware.auth import get_current_user
from src.modules.identity import identity_controller as controller
router = APIRouter(prefix="", tags=["Identity"], dependencies=[Depends(get_current_user)])
ENDPOINTS=[("API_SAVE_PLATFORMUSER","POST","/PlatFormUser/",False),("API_UPDATE_PLATFORMUSER","PUT","/PlatFormUser/updateplatformuser",False),("API_GET_PLATFORMUSERS","GET","/PlatFormUser/fetchallplatformusers",True),("API_GET_ROLES","GET","/PlatFormUser/fetchroleall",True),("API_GET_DESIGNATIONS","GET","/PlatFormUser/fetchdesignationall",True),("API_SAVE_EMPLOYEE","POST","/Employee/createuser",False),("API_UPDATE_EMPLOYEE","PUT","/Employee/updateuser",False),("API_GET_EMPLOYEES","GET","/Employee/fetchusers",True),("API_GET_ACCESSROLES","GET","/fetchuserroleall",True),("API_VIEW_WIP","GET","/viewwip",True),("API_GET_PRESIGNED_URL","GET","/s3upload",True)]
for n,m,p,c in ENDPOINTS:
    async def h(_n=n,_p=p,_c=c): return await controller.handle(_n,_p,_c)
    getattr(router,m.lower())(p,name=n)(h)
