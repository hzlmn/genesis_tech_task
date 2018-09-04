import asyncio

import pytest

from project.helpers import setup_mongo
from project.server import AiohttpServer

tags = [{"tag": "toyota"}, {"tag": "toyota corolla"}, {"tag": "audi"}, {"tag": "audi a8"}]


@pytest.fixture
def collection():
    return "tags"


@pytest.fixture
async def loop():
    return asyncio.get_event_loop()


@pytest.fixture
def config():
    from configs.test import Config
    return Config()


@pytest.fixture
async def mongo(loop, config, collection):
    database = await setup_mongo(config)
    await database.drop_collection(collection)

    await database[collection].insert_many(tags)

    return database


@pytest.fixture
async def client(loop, mongo, config, aiohttp_client):
    from configs.test import Config
    server = AiohttpServer(Config(), loop=loop)
    await server.setup()
    return await aiohttp_client(server.app)
