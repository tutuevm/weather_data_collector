from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class WeatherData(Base):
    __tablename__ = "weather_data"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )
    temperature: Mapped[float] = mapped_column(nullable=False)
    wind_direction: Mapped[int] = mapped_column(nullable=False)
    wind_speed: Mapped[float] = mapped_column(nullable=False)
