import aiohttp
import passlib

from aiolambda.typing import Maybe, Error

from example.db import get_user
from example.user import User


async def check_password(request: aiohttp.web.Request) -> Maybe[User]:
    user_data = await get_user(request)
    if isinstance(user_data, Error):
        return user_data

    user_request = User(**(await request.json()))
    is_verified = passlib.hash.pbkdf2_sha256.verify(user_request.password, user_data.password)
    if not is_verified:
        return Error("'password does not match'", 422)

    return user_request
