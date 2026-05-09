from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_KEY: SecretStr = Field(...)
    API_BASE_URL: str = Field(...)

    model_config = SettingsConfigDict(env_file=".env")