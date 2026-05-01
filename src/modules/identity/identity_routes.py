from fastapi import APIRouter, Depends, Query
from src.core.middleware.auth import get_current_user
from src.modules.identity import identity_controller as controller
platform_router = APIRouter(prefix='/PlatFormUser',tags=['PlatFormUser'],dependencies=[Depends(get_current_user)])
employee_router = APIRouter(prefix='/Employee',tags=['Employee'],dependencies=[Depends(get_current_user)])

@platform_router.post('/', name='API_SAVE_PLATFORMUSER')
async def save_platform_user(): return await controller.handle('API_SAVE_PLATFORMUSER','/',False)
@platform_router.put('/updateplatformuser', name='API_UPDATE_PLATFORMUSER')
async def upd_platform_user(): return await controller.handle('API_UPDATE_PLATFORMUSER','/updateplatformuser',False)
@platform_router.get('/fetchallplatformusers', name='API_GET_PLATFORMUSERS')
async def get_platform_users(PageNumber:int=Query(1),PageSize:int=Query(1000)): return await controller.handle('API_GET_PLATFORMUSERS',f'/fetchallplatformusers?PageNumber={PageNumber}&PageSize={PageSize}',True)
@platform_router.get('/fetchroleall', name='API_GET_ROLES')
async def roles(PageNumber:int=Query(1),PageSize:int=Query(100)): return await controller.handle('API_GET_ROLES',f'/fetchroleall?PageNumber={PageNumber}&PageSize={PageSize}',True)
@platform_router.get('/fetchdesignationall', name='API_GET_DESIGNATIONS')
async def desig(): return await controller.handle('API_GET_DESIGNATIONS','/fetchdesignationall',True)

@employee_router.post('/createuser', name='API_SAVE_EMPLOYEE')
async def save_emp(): return await controller.handle('API_SAVE_EMPLOYEE','/createuser',False)
@employee_router.put('/updateuser', name='API_UPDATE_EMPLOYEE')
async def upd_emp(): return await controller.handle('API_UPDATE_EMPLOYEE','/updateuser',False)
@employee_router.get('/fetchusers', name='API_GET_EMPLOYEES')
async def get_emp(): return await controller.handle('API_GET_EMPLOYEES','/fetchusers',True)
