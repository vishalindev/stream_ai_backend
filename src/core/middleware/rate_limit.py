from slowapi import Limiter
from slowapi.util import get_remote_address
from src.core.config.settings import settings

limiter = Limiter(key_func=get_remote_address, default_limits=[settings.default_rate_limit])
