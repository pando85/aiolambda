from typing import NamedTuple

from aiolambda.functools import bind


class User(NamedTuple):
    username: str
    password: str


@bind
def to_dict(user: User) -> dict:
    return {'username': user.username,
            'password': user.password}
