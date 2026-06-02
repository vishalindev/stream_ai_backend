from typing import Any

from app.core.redis import get_or_set, invalidate_prefix
from app.shared.repository import InMemoryRepository
from app.shared.utils.responses import success_payload


class DomainService:
    def __init__(self, domain: str, repository: InMemoryRepository | None = None):
        self.domain = domain
        self.repository = repository or InMemoryRepository(domain)

    async def execute(
        self,
        api: str,
        path: str,
        *,
        action: str = "read",
        payload: dict[str, Any] | None = None,
        use_cache: bool = True,
    ) -> dict[str, Any]:
        async def resolver() -> dict[str, Any]:
            data: Any = None
            if action == "create":
                data = await self.repository.create(payload or {})
            elif action == "update":
                data = await self.repository.update(payload or {})
            elif action == "list":
                data = await self.repository.list()
            return success_payload(api, path, data=data, cached=False)

        if action in {"create", "update"}:
            await invalidate_prefix(self.domain)
            return await resolver()

        if use_cache:
            result = await get_or_set(f"{self.domain}:{api}:{path}", resolver)
            if isinstance(result, dict):
                result["cached"] = True
            return result
        return await resolver()
