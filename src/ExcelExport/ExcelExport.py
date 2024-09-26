import asyncio
import logging
from typing import List

import pandas as pd
from sqlalchemy import select

from src.WeatherCollector.models import WeatherData
from src.config import BASE_DIR
from src.database import get_async_session

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ExcelExport:
    async def _get_last_ten_records(self) -> List[dict]:
        """Функция для получения последних 10 записей о погоде из БД"""
        async with get_async_session() as session:
            query = (
                select(WeatherData).order_by(WeatherData.created_at.desc()).limit(10)
            )
            res = await session.execute(query)
            result = [row[0] for row in res.all()]
            excel_data = [
                {
                    "created_at": wd.created_at,
                    "temperature": wd.temperature,
                    "wind_direction": wd.wind_direction,
                    "wind_speed": wd.wind_speed,
                }
                for wd in result
            ]
            return excel_data

    def _write_to_excel(self, excel_data: list):
        """Функция для записи данных о погоде в excel"""
        excel_path = BASE_DIR / "data" / "output.xlsx"
        try:
            pd.DataFrame(excel_data).to_excel(excel_path, index=False)
        except PermissionError:
            logger.error(
                "Access to the file is blocked. Please close the file and try again."
            )

    async def get_data_and_write_excel(self):
        logger.info("Starting to get data from db")
        excel_data = await self._get_last_ten_records()
        logger.info("Starting to write excel file")
        await asyncio.to_thread(self._write_to_excel, excel_data)
