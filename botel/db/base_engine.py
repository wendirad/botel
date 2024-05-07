from sqlalchemy import Engine


class SingleTon:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


# TODO: finish emplementation of the sql engine for sql db connections
class SQLBaseEngine(Engine, SingleTon):
    pass


# TODO: create a mongo db parent class for getting mongo connections
class NoSQLBaseEngine:
    pass
