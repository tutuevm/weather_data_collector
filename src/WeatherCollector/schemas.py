from datetime import datetime

from pydantic import BaseModel


class WeatherDataSchema(BaseModel):
    temperature: float
    wind_direction: str
    wind_speed: float
    weather_condition: str
    created_at: datetime
