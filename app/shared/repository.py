from typing import Any

from app.shared.models import memory_store


class InMemoryRepository:
    def __init__(self, domain: str):
        self.domain = domain

    async def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        return memory_store.create(self.domain, payload)

    async def update(self, payload: dict[str, Any]) -> dict[str, Any]:
        return memory_store.update(self.domain, payload)

    async def list(self) -> list[dict[str, Any]]:
        return memory_store.list_items(self.domain)
