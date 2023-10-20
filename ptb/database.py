from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from config import Settings


engine = create_async_engine(url=Settings.db_url, echo=True, future=True)
session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)