import os
from typing import Union

from aiohttp import web

__version__ = "1.0"


async def handler(request: web.Request) -> web.Response:
    return web.json_response({
        "service": "Test Package",
        "version": __version__,
        "build": request.config_dict["build"],
    })


def get_build() -> Union[str, None]:
    try:
        with open(os.path.join(os.path.dirname(__file__), "build_info")) as f:
            return f.read().strip()
    except FileNotFoundError:
        pass


def create_application() -> web.Application:
    application = web.Application()
    application.router.add_get("/api/service", handler)
    application["build"] = get_build()
    return application
