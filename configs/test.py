from dataclasses import dataclass

from .dev import Config as DevConfig


@dataclass
class Config(DevConfig):

    MONGO_HOST: str = "127.0.0.1"

    DB_NAME: str = "test_db"
