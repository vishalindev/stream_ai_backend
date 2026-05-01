from src.modules.dashboard import dashboard_service as service


async def handle(api: str, path: str, use_cache: bool = True):
    return await service.execute(api, path, use_cache)
