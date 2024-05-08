import logging
from core import config
from sqlalchemy import create_engine
from .mongo import MongoDBConnection

logger = config.LOGGER


class EngineFactory(object):
    _db_config = config.DATABASE

    @classmethod
    def get_engine(cls):
        engine = cls._db_config["default"]["ENGINE"]
        name = cls._db_config["default"]["NAME"]
        if engine == "sqlite3":
            logger.debug("Creating sqlite db engine")
            logger.debug(f"Name {name}")
            return create_engine("sqlite+pysqlite:///" + str(name))
        elif engine == "mysql":
            username = cls._db_config["default"]["USER"]
            password = cls._db_config["default"]["PASSWORD"]
            host = cls._db_config["default"]["HOST"]
            port = cls._db_config["default"]["PORT"]
            return create_engine(
                f"mysql+mysqldb://{username}:{password}@{host}:{port}/{name}"
            )
        elif engine == "postgresql":
            username = cls._db_config["default"]["USER"]
            password = cls._db_config["default"]["PASSWORD"]
            host = cls._db_config["default"]["HOST"]
            port = cls._db_config["default"]["PORT"]
            return create_engine(
                f"postgresql://{username}:{password}@{host}:{port}/{name}"
            )
        elif engine == "mongodb":
            return MongoDBConnection()
        else:
            raise ValueError("Unsupported database engine")
