import logging
from typing_extensions import Literal


class BaseFormatter(logging.Formatter):

    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"
    GREEN = "\x1b[32;20m"
    BLUE = "\x1b[34;20m"
    format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s [%(filename)s:%(lineno)d]"

    FORMATS = {
        logging.DEBUG: BLUE + format + RESET,
        logging.INFO: GREEN + format + RESET,
        logging.WARNING: YELLOW + format + RESET,
        logging.ERROR: RED + format + RESET,
        logging.CRITICAL: BOLD_RED + format + RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class BaseLogger(logging.Logger):
    base_handler = logging.StreamHandler()
    base_handler.setFormatter(BaseFormatter())

    def __init__(self, name: str, level: int | str = 0) -> None:
        super().__init__(name, level)
        self.addHandler(self.base_handler)
