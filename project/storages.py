class TagStorage:

    def __init__(self, loop, mongo):
        self.loop = loop
        self.collection = mongo["tags"]

    async def get_tags(self, text):
        async for doc in self.collection.find({
                "$text": {"$search": text}}):
            yield doc
