import aiohttp
import asyncpg
import passlib.hash

from toolz import curry
from typing import Callable

from aiolambda import logger
from aiolambda.db import _check_table_exists
from aiolambda.errors import ObjectAlreadyExists, ObjectNotFound
from aiolambda.typing import Maybe

from auth.config import ADMIN_USER, ADMIN_PASSWORD
from auth.user import User

USERS_TABLE_NAME = 'users'


async def _create_user(conn: asyncpg.connect, user: User) -> Maybe[User]:
    try:
        await conn.execute(f'''
            INSERT INTO {USERS_TABLE_NAME}(username, password) VALUES($1, $2)
        ''', user.username, passlib.hash.pbkdf2_sha256.hash(user.password))
    except asyncpg.exceptions.UniqueViolationError:
        return ObjectAlreadyExists()
    return user


async def _update_user(conn: asyncpg.connect, user: User) -> Maybe[User]:
    await conn.execute(f'''
        UPDATE {USERS_TABLE_NAME} SET password = $2 WHERE username = $1
    ''', user.username, passlib.hash.pbkdf2_sha256.hash(user.password))
    return user


async def _get_user(conn: asyncpg.connection, user: User) -> Maybe[User]:
    row = await conn.fetchrow(
        f'SELECT * FROM {USERS_TABLE_NAME} WHERE username = $1', user.username)

    if not row:
        return ObjectNotFound()
    return User(**dict(row))


async def init_db(conn: asyncpg.connect) -> None:
    if await _check_table_exists(conn, USERS_TABLE_NAME):
        logger.info('Already initializated.')
        return

    logger.info(f'Create table: {USERS_TABLE_NAME}')
    await conn.execute(f'''
        CREATE TABLE {USERS_TABLE_NAME}(
            username text PRIMARY KEY,
            password text
        )
    ''')

    logger.info(f'Create {ADMIN_USER} user')
    await _create_user(conn, User(ADMIN_USER, ADMIN_PASSWORD))


@curry
async def _operate_user(operation: Callable, request: aiohttp.web.Request) -> Maybe[User]:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        maybe_user = await operation(connection, user_request)

    if isinstance(maybe_user, Exception):
        return maybe_user
    return maybe_user


create_user = _operate_user(_create_user)
get_user = _operate_user(_get_user)
update_user = _operate_user(_update_user)
