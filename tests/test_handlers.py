import async_timeout
import pytest
from aiohttp import web


@pytest.mark.parametrize("text,expected_tags", [
    ("The car was toyota and model corolla with sport tunning",
     ["toyota", "toyota corolla"]),
    ("toyota is a great car!",
     ["toyota"]),
    ("toyota is good but audi is better",
     ["toyota", "audi"]),
    ("on sport event audi model a8 easily beat toyota corolla",
     ["toyota", "toyota corolla", "audi", "audi a8"])
])
async def test_main_handler_post(loop, client, text, expected_tags):
    resp = await client.post("/get_tags", json={"text": text})
    data = await resp.json()

    tags = [doc["tag"] for doc in data["tags"]]

    assert tags == expected_tags


async def test_handler_not_found(loop, client):
    resp = await client.post(
        "/get_tags",
        json={
            "text": "some text",
        },
    )

    assert resp.status == web.HTTPNotFound.status_code
