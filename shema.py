from sqlalchemy import BigInteger, String, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///eba.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass
    
class User(Base):
    __tablename__ = 'users'
    
    id1: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    ban: Mapped[bool] = mapped_column(Boolean, default=False)
    reason: Mapped[str] = mapped_column(String, nullable=True)
    
class Problem(Base):
    __tablename__ = 'problems'
    
    id2: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id1: Mapped[int] = mapped_column(BigInteger)
    text: Mapped[str] = mapped_column(String)
    answer: Mapped[str] = mapped_column(String)
    solved: Mapped[bool] = mapped_column(Boolean, default=False)
    
class Review(Base):
    __tablename__ = 'reviews'
    
    id3: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id1: Mapped[int] = mapped_column(BigInteger)
    text: Mapped[str] = mapped_column(String)
    solved: Mapped[bool | None] = mapped_column(Boolean, nullable=True, default=None)
    
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)