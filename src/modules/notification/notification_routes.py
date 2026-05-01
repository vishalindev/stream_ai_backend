from fastapi import APIRouter, Depends
from src.core.middleware.auth import get_current_user
from src.modules.notification import notification_controller as controller
router = APIRouter(prefix="/Notification", tags=["Notification"], dependencies=[Depends(get_current_user)])
ENDPOINTS=[("API_GET_NOTIFICATIONSBYCAMERAID","GET","/fetchnotificationbycameraid",True),("API_GET_NOTIFICATIONBYID","GET","/fetchnotificationbyid",True),("API_GET_NOTIFICATIONARRAY","GET","/getnotificationarray",True),("API_GET_TODAYSNOTIFICATIONS","GET","/fetchnotification",True),("API_POST_NOTIFICATION_STATUS","POST","/notificationstatusupdate",False),("API_SAVE_NOTIFICATIONGROUP","POST","/addnotificationgroup",False),("API_UPDATE_NOTIFICATIONGROUP","PUT","/updatenotificationgroup",False),("API_GET_NOTIFICATIONGROUPS","GET","/fetchnotificationgroupall",True),("API_SAVE_RULE","POST","/addnotificationrule",False),("API_UPDATE_RULE","PUT","/updaterule",False),("API_GET_RULES","GET","/fetchruleall",True),("API_GET_RULEBYUNITID","GET","/fetchrulebyunitid",True)]
for n,m,p,c in ENDPOINTS:
    async def h(_n=n,_p=p,_c=c): return await controller.handle(_n,_p,_c)
    getattr(router,m.lower())(p,name=n)(h)
