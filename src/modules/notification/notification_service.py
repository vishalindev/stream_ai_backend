from src.core.config.redis import get_or_set
from src.core.utils.response import success_payload


async def execute(api: str, path: str, use_cache: bool = True):
    async def resolver():
        return success_payload(api, path)

    if use_cache:
        return await get_or_set(f"dashboard:{api}", resolver)
    return await resolver()
