from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # DATABASE_URL: str
    # SECRET_KEY: str
    # ALGORITHM: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int
    GOOGLE_API_KEY: str
    GEMINI_CHAT_MODEL: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()