import asyncio
import random
import time
import uuid

from configs.base import Config
from project.helpers import setup_mongo


class Script:
    def __init__(self, config):
        self.config = config

    async def populate(self):
        mongo = await setup_mongo(self.config)

        await mongo.drop_collection("tags")

        collection = mongo["tags"]

        tags = [{"tag": str(uuid.uuid4())[:5]} for _ in range(int(1e6))]

        to_insert = [{"tag": value}
                     for value in ["toyota", "toyota supra", "audi"]]

        tags += to_insert

        start_time = time.time()
        result = await collection.insert_many(tags)
        end_time = time.time()
        print(
            f"Inserted {len(result.inserted_ids)} docs in {int(end_time - start_time)}secs")


def entrypoint():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Script(Config()).populate())
