from dataclasses import dataclass

from .base import Config as BaseConfig


@dataclass
class Config(BaseConfig):

    DEBUG: bool = True

    MONGO_HOST: str = "mongo"
