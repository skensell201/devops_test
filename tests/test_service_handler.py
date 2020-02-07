from aiohttp.test_utils import TestClient


async def test(client: TestClient):
    async with client.get("/api/service") as resp:
        assert resp.status == 200
        data = await resp.json()

    assert set(data) == {"service", "version", "build"}
