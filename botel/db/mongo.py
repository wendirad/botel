import motor.motor_asyncio
from urllib.parse import quote_plus
from core import config
from pymongo.server_api import ServerApi


class SingleTon:
    """Singleton class for creating only one database instance for the database connection."""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class MongoDBConnection(SingleTon):
    def __init__(self) -> None:
        self.db = self.get_database()

    def get_client(self):
        _DATABASE_URL_SCHEME = config.DATABASE["DATABASE"]["default"][
            "DATABASE_URL_SCHEME"
        ]
        _DATABASE_USERNAME = config.DATABASE["DATABASE"]["default"][
            "DATABASE_USERNAME"
        ]
        _DATABASE_PASSWORD = config.DATABASE["DATABASE"]["default"][
            "DATABASE_PASSWORD"
        ]
        _DATABASE_SUFFIX = config.DATABASE["DATABASE"]["default"][
            "DATABASE_SUFFIX"
        ]
        return motor.motor_asyncio.AsyncIOMotorClient(
            f"{_DATABASE_URL_SCHEME}://{quote_plus(_DATABASE_USERNAME)}:{quote_plus(_DATABASE_PASSWORD)}{_DATABASE_SUFFIX}",
            serverSelectionTimeoutMS=config.DATABASE["DATABASE"]["default"][
                "DATABASE_SELECTION_TIMEOUT"
            ],
            server_api=ServerApi("1"),
        )

    def get_database(self):
        _DATABASE_NAME = config.DATABASE["DATABASE"]["default"][
            "DATABASE_NAME"
        ]
        return self.get_client().get_database(_DATABASE_NAME)

    def get_collection(self, collection_name):
        
        return self.db.get_collection(collection_name)
