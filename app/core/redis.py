import json
from typing import Any, Awaitable, Callable

from redis.asyncio import Redis

from app.core.config import settings

redis_client: Redis | None = None


async def init_redis() -> None:
    """Initialize Redis if it is reachable; continue without cache otherwise."""
    global redis_client
    redis_client = Redis.from_url(settings.redis_url, decode_responses=True)
    try:
        await redis_client.ping()
    except Exception:
        await redis_client.aclose()
        redis_client = None


async def close_redis() -> None:
    global redis_client
    if redis_client is not None:
        await redis_client.aclose()
        redis_client = None


async def get_or_set(key: str, resolver: Callable[[], Awaitable[Any]], ttl_seconds: int | None = None) -> Any:
    """Return a cached value when Redis is available, otherwise resolve fresh data."""
    if redis_client is None:
        return await resolver()

    cached = await redis_client.get(key)
    if cached is not None:
        return json.loads(cached)

    result = await resolver()
    await redis_client.set(key, json.dumps(result, default=str), ex=ttl_seconds or settings.redis_cache_ttl_seconds)
    return result


async def invalidate_prefix(prefix: str) -> None:
    """Best-effort cache invalidation for a domain prefix."""
    if redis_client is None:
        return
    async for key in redis_client.scan_iter(f"{prefix}:*"):
        await redis_client.delete(key)
