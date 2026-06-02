from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or `.env`."""

    app_name: str = "Stream AI Backend"
    api_prefix: str = ""
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    redis_url: str = "redis://localhost:6379/0"
    redis_cache_ttl_seconds: int = 120
    default_rate_limit: str = "100/minute"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
