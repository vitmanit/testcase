from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
DATABASE_URL = 'postgresql+asyncpg://postgres:!Admin123@db:5432/testcase'
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass