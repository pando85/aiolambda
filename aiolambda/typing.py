from typing import Any, Type, TypeVar, Union, TYPE_CHECKING

from aiolambda.errors import ObjectAlreadyExists, ObjectNotFound


Error = Union[ObjectAlreadyExists, ObjectNotFound]

# Workarround until implementation: https://github.com/python/mypy/issues/5354
CheckError: Type[Any]
if not TYPE_CHECKING:
    CheckError = Error

X = TypeVar('X')
Maybe = Union[X, Error]
