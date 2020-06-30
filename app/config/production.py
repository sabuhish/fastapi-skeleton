from app.config.base import BaseSettings
from pydantic import  SecretStr
import os


class ProdSettings(BaseSettings):
    
    debug: bool = False
    ALLOWED_HOSTS: list = []

    DB_PASSWORD: SecretStr = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT",5432)
    DB_USER: str = os.getenv("DB_USER")

    DB_DSN: str = f"asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    DB_POOL_MIN_SIZE: int = 1
    DB_POOL_MAX_SIZE: int  = 16
    DB_ECHO: bool  =  False
    DB_SSL: str = None 
    DB_USE_CONNECTION_FOR_REQUEST: bool = True
    
    DB_RETRY_LIMIT: int = 1
    DB_RETRY_INTERVAL: int = 1

   


prod_settings = ProdSettings()
