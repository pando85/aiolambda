import pytest

from aiolambda.app import get_app


@pytest.fixture
def cli(loop, aiohttp_client):
    app = get_app()
    return loop.run_until_complete(aiohttp_client(app.app))


async def test_auth(cli):
    token_start = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhaW9sYW1iZGEiLC"
    resp = await cli.get('/v1/auth/12')
    assert resp.status == 200
    token = str(await resp.json())
    assert token.startswith(f'{token_start}')


async def test_secret(cli):
    auth_resp = await cli.get('/v1/auth/12')
    response_example = {
        'user_id': '12',
        'secret': 'wbevuec',
        'token_info': {
            'iss': 'aiolambda',
            'iat': 1545340057,
            'exp': 1545340657,
            'sub': '12'}
    }
    token = str(await auth_resp.json())
    auth_header = {'Authorization': f'Bearer {token}'}
    resp = await cli.get('/v1/secret', headers=auth_header)
    assert resp.status == 200
    assert (await resp.json()).keys() == response_example.keys()


async def test_ping(cli):
    resp = await cli.get('/v1/ping')
    assert resp.status == 200
    assert await resp.json() == 'pong'
