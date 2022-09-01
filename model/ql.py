from typing import Optional

import strawberry
from sqlalchemy import select
from strawberry.types import Info

import model.db as db

# from model.db import get_session


@strawberry.type
class Author:
    id: strawberry.ID
    name: str

    # @strawberry.field
    # async def books(self, info: Info) -> list["Book"]:
    #     books = await info.context["books_by_author"].load(self.id)
    #     return [Book.marshal(book) for book in books]

    @classmethod
    def marshal(cls, model: db.Author) -> "Author":
        return cls(id=strawberry.ID(str(model.id)), name=model.name)


@strawberry.type
class AuthorExists:
    message: str = "Author with this name already exists"


@strawberry.type
class AuthorNotFound:
    message: str = "Couldn't find an author with the supplied name"


@strawberry.type
class AuthorNameMissing:
    message: str = "Please supply an author name"


AddAuthorResponse = strawberry.union("AddAuthorResponse", (Author, AuthorExists))


@strawberry.type
class Book:
    id: strawberry.ID
    name: str
    author: Optional[Author] = None

    @classmethod
    def marshal(cls, model: db.Book) -> "Book":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            author=Author.marshal(model.author) if model.author else None,
        )


AddBookResponse = strawberry.union("AddBookResponse", (Book, AuthorNotFound, AuthorNameMissing))

# def get_last_user() -> User:
#     return User(name="Marco")

# async def load_books_by_author(keys: list) -> list[Book]:
#     async with get_session() as s:
#         all_queries = [select(db.Book).where(db.Book.author_id == key) for key in keys]
#         data = [(await s.execute(sql)).scalars().unique().all() for sql in all_queries]
#         print(keys, data)
#     return data

# dataloader = DataLoader(load_fn=load_books_by_author)
# books = await dataloader.load(1)
