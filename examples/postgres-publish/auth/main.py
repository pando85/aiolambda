import aiohttp.web

from aiolambda.app import get_app
from aiolambda.logger import access_logger

from auth.db import init_db
from auth.handlers import routes


def main():
    app = get_app(init_db)
    app.add_routes(routes)

    aiohttp.web.run_app(app, access_log=access_logger)
