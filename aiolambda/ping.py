from aiohttp.web import Request, Response

from aiolambda.functools import compose
from aiolambda import logger
from aiolambda import response


async def ping_handler(request: Request) -> Response:
    return compose(
        logger.debug,
        response.return_response)('"pong"')
