from app.config.base import BaseSettings
import os


class DevSettings(BaseSettings):

    debug: bool = True
    
    DB_NAME: str = os.getenv("DB_NAME")
    DB_DSN: str = f"asyncpg:///{DB_NAME}"
    DB_ECHO: bool = True

    ALLOWED_HOSTS: list = ["*"]


    

dev_settings = DevSettings()
