import json
import logging
import traceback
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "@timestamp": datetime.utcfromtimestamp(record.created).isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if record.exc_info:
            log_record["exc_info"] = ''.join(traceback.format_exception(*record.exc_info))

        if hasattr(record, "extra"):
            log_record.update(record.extra)

        return json.dumps(log_record)


def setup_logger(name="app"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("app.log", encoding="utf-8")
        file_handler.setFormatter(JsonFormatter())

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(JsonFormatter())

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    logger.propagate = False
    return logger


