from typing import NamedTuple


class User(NamedTuple):
    username: str
    password: str


def to_dict(user: User) -> dict:
    return {'username': user.username,
            'password': user.password}
