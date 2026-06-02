from collections import defaultdict
from copy import deepcopy
from typing import Any
from uuid import uuid4

_STORE: dict[str, list[dict[str, Any]]] = defaultdict(list)


def create(domain: str, payload: dict[str, Any]) -> dict[str, Any]:
    item = {"id": payload.get("id") or str(uuid4()), **payload}
    _STORE[domain].append(deepcopy(item))
    return item


def update(domain: str, payload: dict[str, Any]) -> dict[str, Any]:
    item_id = payload.get("id")
    if item_id:
        for item in _STORE[domain]:
            if item.get("id") == item_id:
                item.update(payload)
                return deepcopy(item)
    return create(domain, payload)


def list_items(domain: str) -> list[dict[str, Any]]:
    return deepcopy(_STORE[domain])
