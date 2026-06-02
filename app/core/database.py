"""Monolithic database bootstrap placeholders.

The project keeps the application in one FastAPI process while isolating domain
repository/service/router files. Replace the in-memory repositories with real
SQLAlchemy sessions here when persistent storage is introduced.
"""


def get_database():
    """Placeholder dependency for future database access."""
    return None
