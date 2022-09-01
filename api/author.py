from fastapi import APIRouter
from sqlalchemy import select

import model.db as db
import model.ql as ql
from config import logger
from model.db import get_session

router = APIRouter(prefix="/v1/author")


@logger.catch
@router.get("/")
async def get_authors() -> list[ql.Author]:
    async with get_session() as s:
        query = select(db.Author)
        data = (await s.execute(query)).scalars().unique().all()
    return data
