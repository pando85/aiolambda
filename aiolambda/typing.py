from typing import NamedTuple, Union, TypeVar


class Success(NamedTuple):
    json: dict
    status_code: int


class Error(NamedTuple):
    msg: str
    status_code: int


X = TypeVar('X')
Maybe = Union[X, Error]
