from aiohttp.web import Request, Response, RouteTableDef

from aiolambda import logger
from aiolambda.functools import compose

from example.db import create_user
from example.user import to_dict
from example.response import return_200, return_201
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
        return_201
    )(request)


@routes.post('/user')
async def create_user_handler(request: Request) -> Response:
    return await compose(
        create_user,
        to_dict,
        return_201
    )(request)


@routes.get('/ping')
async def ping_handler(request: Request) -> Response:
    return compose(
        logger.debug,
        return_200)('pong')
