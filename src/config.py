import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = os.environ.get("DB_PORT")


class Config(BaseSettings):
    DB_SETTINGS: DBSettings = DBSettings()
    WEATHER_REQUEST_DELAY_SEC: int = os.environ.get("WEATHER_REQUEST_DELAY_SEC")


config = Config()
