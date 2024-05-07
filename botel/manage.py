import logging
from botel.db.engine_factory import EngineFactory

db = EngineFactory().get_engine()
db.connect()
