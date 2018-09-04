from .base import Config as BaseConfig


class Config(BaseConfig):

    DEBUG = True

    MONGO_HOST: str = "mongo"
