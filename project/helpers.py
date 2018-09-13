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


def setup_mongodb_parser(parser, prefix="mongo_"):
    parser.add_argument(
        f"--{prefix}host",
        type=str,
        dest="MONGO_HOST"
    )

    parser.add_argument(
        f"--{prefix}port",
        type=int,
        dest="MONGO_PORT"
    )

    return parser
