from aiohttp.web import json_response, Request, Response, RouteTableDef

from aiolambda import logger
from aiolambda.functools import compose
from aiolambda.typing import Maybe, Error, Success

from example.db import create_user
from example.token import create_token
from example.verify import check_password

routes = RouteTableDef()


@routes.post('/auth')
async def auth_handler(request: Request) -> Response:
    return await compose(
        check_password,
        logger.debug,
        create_token,
        logger.debug,
        return_response
    )(request)


@routes.post('/user')
async def create_user_handler(request: Request) -> Response:
    return await compose(
        create_user,
        return_response
    )(request)


def return_response(r: Maybe[Success]) -> Response:
    if isinstance(r, Error):
        return json_response(r.msg, status=r.status_code)
    return json_response(r.json, status=r.status_code)
