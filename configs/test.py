from .dev import Config as DevConfig


class Config(DevConfig):

    MONGO_HOST = "127.0.0.1"

    DB_NAME = "test_db"
