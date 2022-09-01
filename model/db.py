from contextlib import asynccontextmanager
from typing import AsyncGenerator, Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from config import logger, settings

# import asyncio

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False, unique=True)

    books: list["Book"] = relationship("Book", lazy="joined", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    author_id: Optional[int] = Column(Integer, ForeignKey(Author.id), nullable=True)

    author: Optional[Author] = relationship(Author, lazy="joined", back_populates="books")


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                logger.debug("Session begun...")
                yield session
                await session.commit()
                logger.debug("Session commited...")
            except SQLAlchemyError as ex:
                await session.rollback()
                logger.debug("Session rollback...")
                raise ex
            finally:
                await session.close()
                logger.debug("Session closed...")


engine = create_async_engine(
    settings.asyncpg_url,
    future=True,
    echo=True,
)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)


# async def drop_and_create():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     await engine.dispose()


# if __name__ == "__main__":
#     """
#     Usage: python -m model.sqlalchemy
#     """
#     logger.critical("Dropping and re/creating tables")
#     asyncio.run(drop_and_create())
#     logger.critical("Done.")
