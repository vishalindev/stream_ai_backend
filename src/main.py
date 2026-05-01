from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from src.core.config.settings import settings
from src.core.config.redis import init_redis, close_redis
from src.core.middleware.auth import authenticate_user, create_access_token
from src.core.middleware.rate_limit import limiter
from src.modules.dashboard.dashboard_routes import router as dashboard_router, reports_router
from src.modules.camera.camera_routes import router as camera_router
from src.modules.zone.zone_routes import router as zone_router, plant_router
from src.modules.notification.notification_routes import notification_router, notification_group_router, rule_router
from src.modules.identity.identity_routes import platform_router, employee_router

app = FastAPI(title=settings.app_name)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.on_event("startup")
async def startup(): await init_redis()
@app.on_event("shutdown")
async def shutdown(): await close_redis()

@app.post("/auth/token", tags=["Auth"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user: return {"error": "invalid_credentials"}
    return {"access_token": create_access_token(user["username"]), "token_type": "bearer"}

for r in [dashboard_router, reports_router, camera_router, zone_router, plant_router, notification_router, notification_group_router, rule_router, platform_router, employee_router]:
    app.include_router(r)
