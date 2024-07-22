from pathlib import Path
from decouple import config
from .logger import BaseLogger

TOKEN = config("TOKEN")

ROOT_DIR = Path(__file__).resolve().parent.parent

LOGGER = BaseLogger("main_logger")

DATABASE = {
    "default": {
        "ENGINE": "sqlite3",
        "NAME": ROOT_DIR / "db.sqlite3",
    }
}
