from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from src.config import Settings
import asyncio
import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async_engine = create_async_engine(
    url=Settings.DATABASE_URL_psycopg,
    echo=False,
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass