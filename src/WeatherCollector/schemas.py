from pydantic import BaseModel


class WeatherData(BaseModel):
    temperature: float
    wind_direction: int
    wind_speed: float
