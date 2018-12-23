from aiohttp.web import Application
from aio_pika import connect_robust, IncomingMessage
from toolz import curry
from typing import Callable, Dict, Optional

from aiolambda.config import RABBIT_HOST, RABBIT_USER, RABBIT_PASSWORD


# last argument is passed by aiohttp on_startup, this reference is not global
@curry
async def setup_mq_base(queues: Optional[Dict[str, Callable[[IncomingMessage], None]]],
                        app: Application,
                        _useless_reference: Application) -> None:
    rabbit_url = f"amqp://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_HOST}/"
    app['mq'] = {}
    app['mq']['connection'] = await connect_robust(rabbit_url)
    app['mq']['channel'] = await app['mq']['connection'].channel()

    if queues:
        for queue_name, callback in queues.items():
            queue = await app['mq']['channel'].declare_queue(queue_name)
            await queue.consume(callback)
