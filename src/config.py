from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MYSQL_DB_URL : str
    JWT_SECRET : str
    JWT_ALGORITHM : str
    model_config = SettingsConfigDict(
        env_file = Path(__file__).parent.parent / ".env",
        extra = "ignore"
    ) # attribute that will allow us to change the attributes of the pydantic model classes

Config = Settings()


