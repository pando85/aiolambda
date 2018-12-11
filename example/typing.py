from typing import Any, Type, TypeVar, Union, TYPE_CHECKING

from aiolambda import typing
from aiolambda.errors import ObjectAlreadyExists, ObjectNotFound

from example.errors import InvalidPassword


Error = Union[ObjectAlreadyExists, ObjectNotFound, InvalidPassword]
# Workarround until implementation: https://github.com/python/mypy/issues/5354
CheckError: Type[Any]
if not TYPE_CHECKING:
    CheckError = Error

X = TypeVar('X')
Maybe = Union[X, Error]
