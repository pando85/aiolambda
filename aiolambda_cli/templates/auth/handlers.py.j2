from aiohttp.web import Request, Response, RouteTableDef

from aiolambda import logger
from aiolambda.functools import compose

from auth.db import create_user
from auth.user import to_dict
from auth.response import return_200, return_201
from auth.token import create_token
from auth.verify import check_password

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
