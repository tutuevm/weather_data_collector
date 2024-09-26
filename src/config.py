import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
WEATHER_CODES = {
    0: "Чистое небо",
    1: "Преимущественно ясно, переменная облачность, пасмурно",
    2: "Преимущественно ясно, переменная облачность, пасмурно",
    3: "Преимущественно ясно, переменная облачность, пасмурно",
    45: "Туман и отложенный изморозный туман",
    48: "Туман и отложенный изморозный туман",
    51: "Морось: легкая, умеренная и плотная интенсивность",
    53: "Морось: легкая, умеренная и плотная интенсивность",
    55: "Морось: легкая, умеренная и плотная интенсивность",
    56: "Ледяной дождь: легкий и плотный интенсивность",
    57: "Ледяной дождь: легкий и плотный интенсивность",
    61: "Дождь: Небольшая, умеренная и сильная интенсивность",
    63: "Дождь: Небольшая, умеренная и сильная интенсивность",
    65: "Дождь: Небольшая, умеренная и сильная интенсивность",
    66: "Ледяной дождь: легкий и сильный",
    67: "Ледяной дождь: легкий и сильный",
    71: "Снегопад: небольшая, умеренная и сильная интенсивность",
    73: "Снегопад: небольшая, умеренная и сильная интенсивность",
    75: "Снегопад: небольшая, умеренная и сильная интенсивность",
    77: "Снежные зерна",
    80: "Ливневые дожди: слабые, умеренные и сильные",
    81: "Ливневые дожди: слабые, умеренные и сильные",
    82: "Ливневые дожди: слабые, умеренные и сильные",
    85: "Снегопад слабый и сильный",
    86: "Снегопад слабый и сильный",
    95: "Гроза: слабая или умеренная",
    96: "Гроза с небольшим и сильным градом",
    99: "Гроза с небольшим и сильным градом",
}


class DBSettings(BaseModel):
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = os.environ.get("DB_PORT")


class LocationSettings(BaseModel):
    latitude: str = os.environ.get("LATITUDE")
    longitude: str = os.environ.get("LONGITUDE")


class Config(BaseSettings):
    DB_SETTINGS: DBSettings = DBSettings()
    WEATHER_REQUEST_DELAY_SEC: int = os.environ.get("WEATHER_REQUEST_DELAY_SEC")
    LOCATION_SETTINGS: LocationSettings = LocationSettings()


config = Config()
