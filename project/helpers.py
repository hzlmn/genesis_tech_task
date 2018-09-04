async def setup_mongo_index(database):
    import pymongo
    await database["tags"].create_index([
        ("tag", pymongo.TEXT),
    ], background=True)


async def setup_mongo(config):
    import motor.motor_asyncio

    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{config.MONGO_HOST}:{config.MONGO_PORT}")

    database = client[config.DB_NAME]

    await setup_mongo_index(database)

    return database


def lookup_word(word, text, words_shift=2):
    word = word.strip().split(" ")
    text = text.strip().split(" ")

    cursor = 0
    index = 0
    skipped = 0

    while cursor < len(text):
        curr_word = text[cursor]
        part = word[index]

        if curr_word == part:
            if index == len(word) - 1:
                return True

            skipped = 0
            index += 1
        else:
            if skipped < words_shift:
                skipped += 1
            else:
                index = 0
                skipped = 0

        cursor += 1

    return False
