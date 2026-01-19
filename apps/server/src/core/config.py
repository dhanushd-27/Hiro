from functools import lru_cache
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore"
  )

  POSTGRES_USER: str
  POSTGRES_PASSWORD: str
  POSTGRES_DB: str
  POSTGRES_HOST: str = "localhost"
  POSTGRES_PORT: int = 5432


  @computed_field
  @property
  def database_urL(self) -> str:
    return (
      f"postgresql+asyncpg://"
      f"{self.POSTGRES_USER}:"
      f"{self.POSTGRES_PASSWORD}@"
      f"{self.POSTGRES_HOST}:"
      f"{self.POSTGRES_PORT}/"
      f"{self.POSTGRES_DB}"
    )

@lru_cache
def get_settings() -> Settings:
  return Settings()