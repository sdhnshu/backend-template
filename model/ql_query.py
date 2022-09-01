import strawberry
from sqlalchemy import select

import model.db as db
import model.ql as ql
from config import logger
from model.db import get_session


@strawberry.type
class Query:
    @strawberry.field
    async def books(self) -> list[ql.Book]:
        async with get_session() as s:
            sql = select(db.Book).order_by(db.Book.name)
            db_books = (await s.execute(sql)).scalars().unique().all()
        return [ql.Book.marshal(book) for book in db_books]

    @strawberry.field
    async def authors(self) -> list[ql.Author]:
        async with get_session() as s:
            sql = select(db.Author).order_by(db.Author.name)
            db_authors = (await s.execute(sql)).scalars().unique().all()
        return [ql.Author.marshal(loc) for loc in db_authors]
