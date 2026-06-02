"""Backward-compatible ASGI entrypoint.

Prefer running `uvicorn app.main:app --reload` for the new monolithic layout.
"""

from app.main import app

__all__ = ["app"]
