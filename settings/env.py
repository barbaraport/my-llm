from enum import Enum

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class AvailableModels(str, Enum):
    LLAMA_3_2 = "llama3.2"
    DEEPSEEK_R1_1_5 = "deepseek-r1:1.5b"
    DEEPSEEK_V4_FLASH_FREE = "deepseek-v4-flash:free"
    GPT_OSS_120b_FREE = "openai/gpt-oss-120b:free"
    ANY = "openrouter/free"

class Settings(BaseSettings):
    API_KEY: SecretStr = Field(...)
    API_BASE_URL: str = Field(...)
    MODEL_NAME: AvailableModels = Field(...)
    CATALOGUE_URL: str = Field(...)

    model_config = SettingsConfigDict(env_file=".env")