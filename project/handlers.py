from aiohttp import web

from .algo import lookup_word
from .trafarets import GetTagsTrafaret, TagsOutputTrafaret


class MainHandler:

    def __init__(self, loop, app, storage):
        self.loop = loop
        self.app = app
        self.storage = storage

    async def get_tags(self, request):
        post = await request.json()
        data = GetTagsTrafaret(post)

        results = []

        async for doc in self.storage.get_tags(data["text"]):
            if lookup_word(doc["tag"], data["text"]):
                results.append(doc)

        if not results:
            raise web.HTTPNotFound

        return web.json_response(
            TagsOutputTrafaret({
                "tags": results,
            }),
        )
