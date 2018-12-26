import asyncio
import connexion
import uvloop
import os

from typing import Callable, Dict, Optional

from aiolambda.config import API_SPECS_PATH
from aiolambda.db import setup_db_base
from aiolambda.mq import setup_mq_base

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def get_app(init_db: Callable = None,
            init_mq: Optional[Dict[str, Callable]] = None) -> connexion.AioHttpApp:
    app = connexion.AioHttpApp(__name__)
    api = app.add_api(os.path.join(os.getcwd(), API_SPECS_PATH),
                      pass_context_arg_name='request',
                      strict_validation=True)
    if init_db:
        app.app.on_startup.append(setup_db_base(init_db, api.subapp))
    if isinstance(init_mq, dict):
        app.app.on_startup.append(setup_mq_base(init_mq, api.subapp))

    return app
