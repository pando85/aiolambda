import pytest

from aiolambda.app import get_app

from example.db import init_db
from example.handlers import routes


@pytest.fixture
def cli(loop, aiohttp_client):
    app = get_app(init_db)
    app.add_routes(routes)
    return loop.run_until_complete(aiohttp_client(app))


async def test_aiolambda(cli):
    resp = await cli.post('/auth', json={'username': 'admin', 'password': 'admin'})
    assert resp.status == 200
    assert await resp.json() == {'token': 'TODO'}


async def test_aiolambda_incorret_user(cli):
    resp = await cli.post('/auth', json={'username': 'foo', 'password': 'foo'})
    assert resp.status == 422
    assert await resp.json() == "'user does not exists'"


async def test_aiolambda_incorret_password(cli):
    resp = await cli.post('/auth', json={'username': 'admin', 'password': 'foo'})
    assert resp.status == 422
    assert await resp.json() == "'password does not match'"


async def test_user_add(cli):
    user = {'username': 'test2', 'password': 'test1234'}
    resp = await cli.post('/user', json=user)
    assert resp.status == 201
    assert await resp.json() == user


async def test_user_add_exist_user(cli):
    user = {'username': 'admin', 'password': 'test1234'}
    resp = await cli.post('/user', json=user)
    assert resp.status == 200
    assert await resp.json() == user
