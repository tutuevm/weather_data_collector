from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.config import config

DB_URL = f"postgresql+asyncpg://{config.DB_SETTINGS.DB_USER}:{config.DB_SETTINGS.DB_PASS}@{config.DB_SETTINGS.DB_HOST}:{config.DB_SETTINGS.DB_PORT}/{config.DB_SETTINGS.DB_NAME}"


async_engine = create_async_engine(url=DB_URL)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    __abstract__ = True


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
