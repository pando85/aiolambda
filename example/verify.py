import aiohttp
import passlib


from example.db import get_user
from example.errors import InvalidPassword
from example.typing import Maybe
from example.user import User


async def check_password(request: aiohttp.web.Request) -> Maybe[User]:
    user_data = await get_user(request)
    if not isinstance(user_data, User):
        return user_data

    user_request = User(**(await request.json()))
    is_verified = passlib.hash.pbkdf2_sha256.verify(user_request.password, user_data.password)
    if not is_verified:
        return InvalidPassword()

    return user_request
