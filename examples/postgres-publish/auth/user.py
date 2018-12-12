from functools import partial
from typing import NamedTuple

from aiolambda.functools import bind


class User(NamedTuple):
    username: str
    password: str


def _to_dict(user: User) -> dict:
    return {'username': user.username,
            'password': user.password}


to_dict = partial(bind, _to_dict)
