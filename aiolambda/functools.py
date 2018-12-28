import functools

from inspect import iscoroutinefunction
from toolz import curry
from typing import Callable, TypeVar

T = TypeVar('T')


def _iscoroutinefunction_or_partial(object):
    if (isinstance(object, functools.partial) or
            isinstance(object, curry) or isinstance(object, bind)):
        return iscoroutinefunction(object.func)
    return iscoroutinefunction(object)


def compose(*funcs: Callable) -> Callable:
    first, second, *rest = funcs
    if rest:
        second = compose(second, *rest)
    if _iscoroutinefunction_or_partial(first) and _iscoroutinefunction_or_partial(second):
        async def _async(*args, **kwargs):
            first_result = first(*args, **kwargs)
            if isinstance(first_result, Exception):
                return first_result
            return await second(await first_result)
        return _async
    if _iscoroutinefunction_or_partial(second):
        async def _async(*args, **kwargs):
            second_result = second(first(*args, **kwargs))
            if isinstance(second_result, Exception):
                return second_result
            return await second_result
        return _async
    if _iscoroutinefunction_or_partial(first):
        async def _async(*args, **kwargs):
            first_result = first(*args, **kwargs)
            if isinstance(first_result, Exception):
                return second(first_result)
            return second(await first_result)
        return _async

    def _func(*args, **kwargs):
        return second(first(*args, **kwargs))
    return _func


class bind(curry):
    def __init__(self, *args, **kwargs):
        exception = self._get_check_error(args)
        if exception:
            return exception
        return curry.__init__(self, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        exception = self._get_check_error(args)
        if exception:
            return exception
        return curry.__call__(self, *args, **kwargs)

    def _get_check_error(self, _list):
        for x in _list:
            if isinstance(x, Exception):
                return x
        return None
