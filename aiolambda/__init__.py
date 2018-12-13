__version__ = '0.0.3'

import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
