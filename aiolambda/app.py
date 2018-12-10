import aiohttp.web

from functools import partial
from typing import Callable, Dict

from aiolambda.db import setup_db_base
from aiolambda.ping import ping_handler
from aiolambda.mq import setup_mq_base


def get_app(init_db: Callable = None,
            init_mq: Dict[str, Callable] = None) -> aiohttp.web.Application:
    app = aiohttp.web.Application()
    if init_db:
        setup_db = partial(setup_db_base, init_db)
        app.on_startup.append(setup_db)
    if init_mq:
        setup_mq = partial(setup_mq_base, init_mq)
        app.on_startup.append(setup_mq)
    app.add_routes([
        aiohttp.web.get('/ping', ping_handler),
    ])

    return app
