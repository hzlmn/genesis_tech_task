from dataclasses import dataclass


@dataclass
class Config:

    TIMEOUT: int = 10

    TIMEOUT: int = 10

    WORKERS_COUNT: int = 10

    PORT: int = 9002

    MONGO_HOST: str = "127.0.0.1"

    MONGO_PORT: int = 27017

    DB_NAME: str = "genesis_task"
