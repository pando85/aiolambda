import pytest

from aiolambda.app import get_app


@pytest.fixture
def cli(loop, aiohttp_client):
    app = get_app()
    return loop.run_until_complete(aiohttp_client(app))

    async def get_application(self):
        return get_app()


async def test_aiolambda(cli):
    resp = await cli.get('/ping')
    assert resp.status == 200
    assert await resp.json() == 'pong'
