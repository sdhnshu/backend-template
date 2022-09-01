from typing import Optional

import strawberry
from sqlalchemy import select

import model.db as db
import model.ql as ql
from model.db import get_session


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_book(self, name: str, author_name: Optional[str]) -> ql.AddBookResponse:
        async with get_session() as s:
            db_author = None
            if author_name:
                sql = select(db.Author).where(db.Author.name == author_name)
                db_author = (await s.execute(sql)).scalars().first()
                if not db_author:
                    return ql.AuthorNotFound()
            else:
                return ql.AuthorNameMissing()
            db_book = db.Book(name=name, author=db_author)
            s.add(db_book)
            await s.commit()
        return ql.Book.marshal(db_book)

    @strawberry.mutation
    async def add_author(self, name: str) -> ql.AddAuthorResponse:
        async with get_session() as s:
            sql = select(db.Author).where(db.Author.name == name)
            existing_db_author = (await s.execute(sql)).first()
            if existing_db_author is not None:
                return ql.AuthorExists()
            db_author = db.Author(name=name)
            s.add(db_author)
            await s.commit()
        return ql.Author.marshal(db_author)
