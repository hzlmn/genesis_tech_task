import asyncio
import logging

import aiohttp_debugtoolbar
from aiohttp import web

from configs.base import Config as BaseConfig

from .handlers import MainHandler
from .helpers import setup_mongo
from .middlewares import validation_middleware
from .routes import setup_main_handler
from .storages import TagStorage

logger = logging.getLogger(__name__)


class AiohttpServer:
    def __init__(self, config, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()

        self.loop = loop

        if not isinstance(config, BaseConfig):
            raise RuntimeError(
                "Config object should be instance of BaseConfig")

        self.config = config

    async def setup(self):
        self.middlewares = [validation_middleware]

        self.app = web.Application(
            loop=self.loop,
            middlewares=self.middlewares,
            debug=self.config.DEBUG,
        )

        if self.config.DEBUG:
            import aiohttp_debugtoolbar

            aiohttp_debugtoolbar.setup(self.app, intercept_redirects=False)

        self.mongo = await setup_mongo(self.config)

        self.storage = TagStorage(self.loop, self.mongo)
        self.handler = MainHandler(self.loop, self.app, self.storage)

        setup_main_handler(self.app, self.handler)

    def start(self):
        if self.config.DEBUG:
            import aioreloader

            aioreloader.start()

        web.run_app(self.app, port=self.config.PORT)

    async def stop(self):
        pass
