import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.ExcelExport.ExcelExport import ExcelExport
from src.WeatherCollector.WeatherCollector import WeatherCollector
from src.config import config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
weather_collector = WeatherCollector()
excel_export = ExcelExport()


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        weather_collector.collect_and_write_data,
        IntervalTrigger(seconds=config.WEATHER_REQUEST_DELAY_SEC),
    )
    scheduler.start()
    while True:
        user_input = await asyncio.to_thread(input, "> ")
        if user_input.strip().lower() == "export":
            logger.info("Command 'export' accepted. Exporting data...")
            await excel_export.get_data_and_write_excel()
        else:
            logger.warning(f"Unknown command: {user_input}")


if __name__ == "__main__":
    try:
        logger.info("Запуск программы.")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Остановка программы.")
