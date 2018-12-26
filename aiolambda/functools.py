import functools

from inspect import iscoroutinefunction
from toolz import curry
from typing import Any, Callable, TypeVar

from aiolambda.typing import Maybe

T = TypeVar('T')


def _iscoroutinefunction_or_partial(object):
    if isinstance(object, functools.partial) or isinstance(object, curry):
        object = object.func
    return iscoroutinefunction(object)


def compose(*funcs: Callable) -> Callable:
    first, second, *rest = funcs
    if rest:
        second = compose(second, *rest)
    if _iscoroutinefunction_or_partial(first) and _iscoroutinefunction_or_partial(second):
        async def _async(*args, **kwargs):
            return await second(await first(*args, **kwargs))
        return _async
    if _iscoroutinefunction_or_partial(second):
        async def _async(*args, **kwargs):
            return await second(first(*args, **kwargs))
        return _async
    if _iscoroutinefunction_or_partial(first):
        async def _async(*args, **kwargs):
            return second(await first(*args, **kwargs))
        return _async

    def _func(*args, **kwargs):
        return second(first(*args, **kwargs))
    return _func


@curry
def bind(f: Callable, x: Maybe[T], extra_arg: Any = None) -> Any:
    if isinstance(x, Exception):
        return x
    if extra_arg:
        return f(x, extra_arg)
    return f(x)
