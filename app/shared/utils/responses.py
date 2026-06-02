from typing import Any


def success_payload(api: str, path: str, data: Any | None = None, cached: bool = False) -> dict[str, Any]:
    return {"api": api, "path": path, "message": "Implement business logic here", "data": data, "cached": cached}
