from pydantic import SecretStr

from settings.env import Settings


env_settings = Settings()

def get_setting(setting_name: str):
    if hasattr(env_settings, setting_name):
        setting_value =  getattr(env_settings, setting_name)

        if isinstance(setting_value, SecretStr):
            return setting_value.get_secret_value()
        
        return setting_value
    else:
        raise AttributeError(f"Setting '{setting_name}' not found in environment settings.")