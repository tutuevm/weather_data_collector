import logging
from datetime import datetime

import aiohttp
from sqlalchemy import insert

from src.WeatherCollector.models import WeatherData
from src.WeatherCollector.schemas import WeatherDataSchema
from src.config import WEATHER_CODES, config
from src.database import get_async_session

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class WeatherCollector:

    def _degrees_to_compass(self, degrees) -> str:
        """Функция перевода углов в направление стороны света"""
        directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
        idx = int((degrees + 22.5) // 45) % 8
        return directions[idx]

    def _parse_weather(self, weather: dict) -> dict:
        """Функция для приведения данных о погоде к нужному виду"""
        weather["time"] = datetime.strptime(weather["time"], "%Y-%m-%dT%H:%M")
        weather["winddirection"] = self._degrees_to_compass(weather["winddirection"])
        weather["weathercode"] = WEATHER_CODES.get(
            weather["weathercode"], "Погода неизвестна"
        )
        return weather

    async def _collect_weather_data(self) -> dict:
        """Функция для получения данных о погоде"""
        async with aiohttp.ClientSession() as session:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={config.LOCATION_SETTINGS.latitude}&longitude={config.LOCATION_SETTINGS.longitude}&current_weather=true&timezone=Europe/Moscow"
            async with session.get(url) as response:
                data = await response.json()
                weather = self._parse_weather(data["current_weather"])
        return weather

    async def _write_data_to_db(self, weather_data: WeatherDataSchema):
        """Функция для записи данных о погоде в БД"""
        data = weather_data.model_dump()
        async with get_async_session() as session:
            stmt = insert(WeatherData).values(**data)
            await session.execute(stmt)
            await session.commit()

    async def collect_and_write_data(self):
        logger.info("starting to receive data")
        client_data = await self._collect_weather_data()
        weather_data = WeatherDataSchema(
            created_at=client_data["time"],
            temperature=float(client_data["temperature"]),
            wind_direction=client_data["winddirection"],
            wind_speed=float(client_data["windspeed"]),
            weather_condition=client_data["weathercode"],
        )
        logger.info("writing data to DB")
        await self._write_data_to_db(weather_data=weather_data)
