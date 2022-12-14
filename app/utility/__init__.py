import logging
import os

import redis

redis_conn = redis.StrictRedis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    password=os.getenv("REDIS_PASS"),
    charset="utf-8", decode_responses=True)


def init_logger(logger_name):
    global log_level
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "DEBUG"
    logging.getLogger(logger_name).setLevel(log_level)
    logging.getLogger().setLevel("INFO")
