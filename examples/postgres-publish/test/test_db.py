import asyncpg
import passlib
import pytest

from aiolambda.config import (POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER,
                              POSTGRES_PASSWORD)

from auth.db import USERS_TABLE_NAME, init_db, _create_user, _get_user
from auth.user import User


@pytest.fixture
async def pool(loop):
    pool = await asyncpg.create_pool(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    async with pool.acquire() as connection:
        await init_db(connection)
    return pool


async def count_rows(conn: asyncpg.connect, table: str):
    r = await conn.fetchrow(f'SELECT COUNT(*) FROM {table}')
    return r['count']


async def test_create_user(pool: asyncpg.pool.Pool):
    test_user = User('test', 'test1234')
    async with pool.acquire() as connection:
        rows_len = await count_rows(connection, USERS_TABLE_NAME)
        await _create_user(connection, test_user)
        rows_len_after = await count_rows(connection, USERS_TABLE_NAME)
    assert (rows_len_after - rows_len) == 1


async def test_get_user(pool: asyncpg.pool.Pool):
    test_user = User('admin', 'admin')
    async with pool.acquire() as connection:
        user = await _get_user(connection, test_user)
    # Avoid mypy complain about types
    if isinstance(user, User):
        assert test_user.username == user.username
        is_verified = passlib.hash.pbkdf2_sha256.verify(test_user.password, user.password)
        assert is_verified is True
        return
