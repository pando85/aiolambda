from aiohttp.web import Response

from aiolambda import logger
from aiolambda.functools import compose

from jwt.response import return_200
from jwt.jwt import generate_token
from jwt.utils import get_secret


async def auth_handler(user_id) -> Response:
    return compose(
        generate_token,
        logger.debug,
        return_200)(user_id)


async def secret_handler(*_null, **request) -> Response:
    return compose(
        get_secret,
        logger.debug,
        return_200)(request)


async def ping_handler() -> Response:
    return compose(
        logger.debug,
        return_200)('pong')
