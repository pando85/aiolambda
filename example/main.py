import aiohttp.web

from aiolambda.app import get_app
from aiolambda.logger import access_logger

from example.db import init_db
from example.handlers import routes


def main():
    app = get_app(init_db)
    app.add_routes(routes)

    aiohttp.web.run_app(app, access_log=access_logger)
