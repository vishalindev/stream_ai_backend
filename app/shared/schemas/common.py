from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class PaginationParams(BaseModel):
    PageNumber: int = Field(1, ge=1)
    PageSize: int = Field(100, ge=1, le=5000)


class DomainPayload(BaseModel):
    """Generic request body for legacy endpoints until concrete schemas are wired."""

    model_config = ConfigDict(extra="allow")
    name: str | None = None
    description: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class EndpointResponse(BaseModel):
    api: str
    path: str
    message: str = "Implement business logic here"
    data: Any | None = None
    cached: bool = False
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
