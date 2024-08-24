from pydantic_settings import BaseSettings
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

class Settings(BaseSettings):
    
    @property
    def DATABASE_URL_asyncpg(self):
        return os.getenv('URL')
    @property
    def DATABASE_URL_psycopg(self):
    # postgresql+psycopg://user:password@host:port/name
        return os.getenv('URL')

Settings = Settings()