from contextlib import asynccontextmanager

from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
from app.core.logging import configure_logging
from app.core.redis import close_redis, init_redis
from app.modules.admin.router import employee_router, plant_router
from app.modules.camera.router import router as camera_router
from app.modules.dashboard.router import router as dashboard_router
from app.modules.identity.router import router as identity_router
from app.modules.mobile.router import router as mobile_router
from app.modules.notification.router import notification_group_router, notification_router
from app.modules.platformuser.router import router as platformuser_router
from app.modules.reports.router import router as reports_router
from app.modules.rule.router import router as rule_router
from app.modules.zone.router import router as zone_router

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=[settings.default_rate_limit])

configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis()
    try:
        yield
    finally:
        await close_redis()


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


for router in [
    identity_router,
    employee_router,
    plant_router,
    platformuser_router,
    camera_router,
    zone_router,
    rule_router,
    notification_group_router,
    notification_router,
    dashboard_router,
    reports_router,
    mobile_router,
]:
    app.include_router(router)
