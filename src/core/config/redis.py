import json
from typing import Any, Awaitable, Callable
from redis.asyncio import Redis
from src.core.config.settings import settings

redis_client: Redis | None = None


async def init_redis() -> None:
    global redis_client
    redis_client = Redis.from_url(settings.redis_url, decode_responses=True)


async def close_redis() -> None:
    if redis_client:
        await redis_client.aclose()


async def get_or_set(key: str, resolver: Callable[[], Awaitable[Any]], ttl_seconds: int = 120) -> Any:
    if redis_client is None:
        return await resolver()
    cached = await redis_client.get(key)
    if cached:
        return json.loads(cached)
    result = await resolver()
    await redis_client.set(key, json.dumps(result), ex=ttl_seconds)
    return result
