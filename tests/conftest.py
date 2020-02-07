from typing import Callable, Awaitable

import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient

from package import create_application


@pytest.fixture
def app() -> web.Application:
    return create_application()


@pytest.fixture
async def client(
        app: web.Application, aiohttp_client: Callable[[web.Application], Awaitable[TestClient]]
) -> TestClient:
    return await aiohttp_client(app)
