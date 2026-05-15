from enum import Enum

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class AvailableModels(str, Enum):
    LLAMA_3_2 = "llama3.2"
    DEEPSEEK_R1_1_5 = "deepseek-r1:1.5b"

class Settings(BaseSettings):
    API_KEY: SecretStr = Field(...)
    API_BASE_URL: str = Field(...)
    MODEL_NAME: AvailableModels = Field(...)
    CATALOGUE_URL: str = Field(...)

    model_config = SettingsConfigDict(env_file=".env")