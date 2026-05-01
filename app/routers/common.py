from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.core.cache import get_or_set


def build_router(tag: str, endpoints: list[tuple[str, str, str]]) -> APIRouter:
    router = APIRouter(prefix=f"/{tag}", tags=[f"{tag} Service"], dependencies=[Depends(get_current_user)])

    for name, method, path in endpoints:
        async def handler(_name=name, _path=path):
            async def resolver():
                return {"api": _name, "path": _path, "message": "Implement business logic here"}

            if _name.startswith("API_GET") or _name.startswith("API_FETCH"):
                return await get_or_set(f"{tag}:{_name}", resolver, ttl_seconds=120)
            return await resolver()

        if method == "GET":
            router.get(path, name=name)(handler)
        elif method == "POST":
            router.post(path, name=name)(handler)
        elif method == "PUT":
            router.put(path, name=name)(handler)
        elif method == "DELETE":
            router.delete(path, name=name)(handler)

    return router
