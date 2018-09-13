import argparse
import asyncio
import logging
import sys

import aiohttp_debugtoolbar
from aiohttp import web

from configs.base import Config as BaseConfig

from .handlers import MainHandler
from .helpers import setup_mongo, setup_mongodb_parser
from .middlewares import validation_middleware
from .routes import setup_main_handler
from .storages import TagStorage

logger = logging.getLogger(__name__)


class AiohttpServer:
    def __init__(self, config, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()

        self.loop = loop
        self.config = config

    def configurate(self):
        options = self.parser.parse_args(sys.argv[1:])

        options = {
            key: value
            for key, value in vars(options).items()
            if value is not None
        }

        config = self.config(**options)

        return config

    def setup_argparse(self):
        parser = setup_mongodb_parser(
            argparse.ArgumentParser("aiohttp-server"))

        parser.add_argument(
            "--port",
            type=int,
            dest="PORT"
        )

        parser.add_argument(
            "--timeout",
            type=int,
            dest="TIMEOUT"
        )

        parser.add_argument(
            "--db_name",
            type=str,
            dest="DB_NAME"
        )

        return parser

    async def setup(self):
        self.parser = self.setup_argparse()

        self.config = self.configurate()

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
