import aiohttp
import passlib

from aiolambda.typing import Maybe

from auth.db import get_user
from auth.errors import InvalidPassword
from auth.user import User


async def check_password(request: aiohttp.web.Request) -> Maybe[User]:
    user_data = await get_user(request)
    if not isinstance(user_data, User):
        return user_data

    user_request = User(**(await request.json()))
    is_verified = passlib.hash.pbkdf2_sha256.verify(user_request.password, user_data.password)
    if not is_verified:
        return InvalidPassword()

    return user_request
