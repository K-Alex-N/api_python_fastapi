import logging
import os
import json
from datetime import datetime

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "@timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
        }

        if hasattr(record, "extra"):
            log_record.update(record.extra)

        return json.dumps(log_record)

def setup_logger():
    logger = logging.getLogger("fastapi_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(os.path.join(log_dir, "app.log"))
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)

    return logger
