import asyncpg

from aiohttp.web import Application
from toolz import curry
from typing import Callable

from aiolambda.config import (POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER,
                              POSTGRES_PASSWORD)


async def _check_table_exists(pool: asyncpg.pool, table: str) -> bool:
    async with pool.acquire() as conn:
        r = await conn.fetchrow(f'''
            SELECT EXISTS (
                SELECT 1
                FROM   pg_tables
                WHERE  schemaname = 'public'
                AND    tablename = $1
                );
        ''', table)
    return r['exists']


# last argument is passed by aiohttp on_startup, this reference is not global
@curry
async def setup_db_base(init_db: Callable,
                        app: Application,
                        _useless_reference: Application) -> None:
    app['pool'] = await asyncpg.create_pool(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    await init_db(app['pool'])
