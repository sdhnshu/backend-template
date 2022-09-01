import requests
from dotenv import load_dotenv

load_dotenv()  # noqa

from config import settings


def test_health():
    resp = requests.get(settings.url)
    assert resp.json() == {"ping": "pong"}
