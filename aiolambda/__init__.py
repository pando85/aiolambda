__version__ = '0.0.6'

import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
