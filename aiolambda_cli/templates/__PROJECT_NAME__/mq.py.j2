from typing import Any, Callable, Dict, Optional

from aio_pika import Channel, DeliveryMode, Message


async def send_message(channel: Channel, message_body: Any) -> None:
    message = Message(
        message_body,
        delivery_mode=DeliveryMode.PERSISTENT
    )

    await channel.default_exchange.publish(
        message, routing_key='task_queue'
    )


def init_mq() -> Optional[Dict[str, Callable]]:
    return {}
