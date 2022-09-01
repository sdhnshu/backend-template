import os
import sys
from functools import lru_cache

from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    url: str = os.getenv("URL", "")
    pg_user: str = os.getenv("SQL_USER", "")
    pg_pass: str = os.getenv("SQL_PASS", "")
    pg_host: str = os.getenv("SQL_HOST", "")
    pg_database: str = os.getenv("SQL_DB", "")
    pg_port: str = os.getenv("SQL_PORT", "")
    asyncpg_url: str = f"postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}:5432/{pg_database}"


config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": (
                "<level>{level}:</level>     <level>{message}</level> <blue>{file}:{function}:"
                "{line}</blue> <green>{time:YYYY-MM-DD HH:mm:ss}</green>"
            ),
            "backtrace": True,
            "diagnose": True,
            "enqueue": True,
        },
        {
            "sink": "logs/{time}.log",
            "format": (
                "<level>{level}:</level>     <level>{message}</level> <blue>{file}:{function}:"
                "{line}</blue> <green>{time:YYYY-MM-DD HH:mm:ss}</green>"
            ),
            # "serialize": True,
            "rotation": "00:00",
            "retention": "30 days",
            "compression": "zip",
            "enqueue": True,
        },
    ],
    # "extra": {"user": "someone"}
}


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
logger.configure(**config)

# logger.debug(settings.asyncpg_url)
