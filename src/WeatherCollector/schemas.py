from pydantic import BaseModel


class WeatherDataSchema(BaseModel):
    temperature: float
    wind_direction: int
    wind_speed: float
