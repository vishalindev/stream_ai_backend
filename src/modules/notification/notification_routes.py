from fastapi import APIRouter, Depends, Query
from src.core.middleware.auth import get_current_user
from src.modules.notification import notification_controller as controller
notification_router = APIRouter(prefix="/Notification", tags=["Notification"], dependencies=[Depends(get_current_user)])
notification_group_router = APIRouter(prefix="/NotificationGroup", tags=["NotificationGroup"], dependencies=[Depends(get_current_user)])
rule_router = APIRouter(prefix="/Rule", tags=["Rule"], dependencies=[Depends(get_current_user)])

@notification_router.get('/fetchnotificationbycameraid', name='API_GET_NOTIFICATIONSBYCAMERAID')
async def by_camera(): return await controller.handle('API_GET_NOTIFICATIONSBYCAMERAID','/fetchnotificationbycameraid',True)
@notification_router.get('/fetchnotificationbyid', name='API_GET_NOTIFICATIONBYID')
async def by_id(): return await controller.handle('API_GET_NOTIFICATIONBYID','/fetchnotificationbyid',True)
@notification_router.get('/getnotificationarray', name='API_GET_NOTIFICATIONARRAY')
async def arr(): return await controller.handle('API_GET_NOTIFICATIONARRAY','/getnotificationarray',True)
@notification_router.get('/fetchnotification', name='API_GET_TODAYSNOTIFICATIONS')
async def today(): return await controller.handle('API_GET_TODAYSNOTIFICATIONS','/fetchnotification',True)
@notification_router.post('/notificationstatusupdate', name='API_POST_NOTIFICATION_STATUS')
async def upd_status(): return await controller.handle('API_POST_NOTIFICATION_STATUS','/notificationstatusupdate',False)

@notification_group_router.post('/addnotificationgroup', name='API_SAVE_NOTIFICATIONGROUP')
async def save_group(): return await controller.handle('API_SAVE_NOTIFICATIONGROUP','/addnotificationgroup',False)
@notification_group_router.put('/updatenotificationgroup', name='API_UPDATE_NOTIFICATIONGROUP')
async def upd_group(): return await controller.handle('API_UPDATE_NOTIFICATIONGROUP','/updatenotificationgroup',False)
@notification_group_router.get('/fetchnotificationgroupall', name='API_GET_NOTIFICATIONGROUPS')
async def all_groups(PageNumber:int=Query(1),PageSize:int=Query(1000)): return await controller.handle('API_GET_NOTIFICATIONGROUPS',f'/fetchnotificationgroupall?PageNumber={PageNumber}&PageSize={PageSize}',True)

@rule_router.post('/addnotificationrule', name='API_SAVE_RULE')
async def save_rule(): return await controller.handle('API_SAVE_RULE','/addnotificationrule',False)
@rule_router.put('/updaterule', name='API_UPDATE_RULE')
async def upd_rule(): return await controller.handle('API_UPDATE_RULE','/updaterule',False)
@rule_router.get('/fetchruleall', name='API_GET_RULES')
async def rules(PageNumber:int=Query(1),PageSize:int=Query(100)): return await controller.handle('API_GET_RULES',f'/fetchruleall?PageNumber={PageNumber}&PageSize={PageSize}',True)
@rule_router.get('/fetchrulebyunitid', name='API_GET_RULEBYUNITID')
async def rule_unit(): return await controller.handle('API_GET_RULEBYUNITID','/fetchrulebyunitid',True)
