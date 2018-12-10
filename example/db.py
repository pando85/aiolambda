import aiohttp
import asyncpg
import passlib.hash

from aiolambda import logger
from aiolambda.db import _check_table_exists
from aiolambda.typing import Maybe, Error, Success

from example.config import ADMIN_USER, ADMIN_PASSWORD
from example.user import User, to_dict

USERS_TABLE_NAME = 'users'


async def _create_user(conn: asyncpg.connect, user: User) -> Maybe[User]:
    try:
        await conn.execute(f'''
            INSERT INTO {USERS_TABLE_NAME}(username, password) VALUES($1, $2)
        ''', user.username, passlib.hash.pbkdf2_sha256.hash(user.password))
    except asyncpg.exceptions.UniqueViolationError:
        return Error("'user already exists'", 409)
    return user


async def _update_user(conn: asyncpg.connect, user: User) -> Maybe[User]:
    await conn.execute(f'''
        UPDATE {USERS_TABLE_NAME} SET password = $2 WHERE username = $1
    ''', user.username, passlib.hash.pbkdf2_sha256.hash(user.password))
    return user


async def _get_user(conn: asyncpg.connection, username: str) -> Maybe[User]:
    row = await conn.fetchrow(
        f'SELECT * FROM {USERS_TABLE_NAME} WHERE username = $1', username)

    if not row:
        return Error("'user does not exists'", 422)
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

    logger.info(f'Create admin user')
    await _create_user(conn, User(ADMIN_USER, ADMIN_PASSWORD))


async def create_user(request: aiohttp.web.Request) -> Maybe[Success]:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        maybe_user = await _create_user(connection, user_request)
        if isinstance(maybe_user, User):
            return Success(to_dict(maybe_user), 201)
        maybe_user = await _update_user(connection, user_request)
        if isinstance(maybe_user, User):
            return Success(to_dict(maybe_user), 200)
    return maybe_user


async def get_user(request: aiohttp.web.Request) -> Maybe[User]:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        user = await _get_user(connection, user_request.username)
    return user
