import logging

import aiohttp
from sqlalchemy import insert

from src.WeatherCollector.models import WeatherData
from src.database import get_async_session

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class WeatherCollector:

    async def _collect_weather_data(self):
        async with aiohttp.ClientSession() as session:
            url = "https://api.open-meteo.com/v1/forecast?latitude=55.6878&longitude=37.3684&current_weather=true"
            async with session.get(url) as response:
                data = await response.json()
                weather = data["current_weather"]
        return weather

    async def _write_data_to_db(self, weather_data: WeatherData):
        async with get_async_session() as session:
            stmt = insert(WeatherData).values(**weather_data)
            await session.execute(stmt)
            await session.commit()

    async def collect_and_write_data(self):
        logger.info("starting to receive data")
        client_data = await self._collect_weather_data()
        weather_data = WeatherData(
            temperature=client_data["temperature"],
            wind_direction=client_data["winddirection"],
            wind_speed=client_data["windspeed"],
        )
        logger.info("writing data to DB")
        await self._write_data_to_db(weather_data=weather_data)
