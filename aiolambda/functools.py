from inspect import iscoroutinefunction
from typing import Any, Callable, TypeVar

from aiolambda.typing import Maybe, CheckError

T = TypeVar('T')


def compose(*funcs: Any) -> Callable:
    first, second, *rest = funcs
    if rest:
        second = compose(second, *rest)
    if iscoroutinefunction(first) and iscoroutinefunction(second):
        async def _async(*args, **kwargs):
            return await second(await first(*args, **kwargs))
        return _async
    if iscoroutinefunction(first):
        async def _async(*args, **kwargs):
            return second(await first(*args, **kwargs))
        return _async

    def _func(*args, **kwargs):
        return second(first(*args, **kwargs))
    return _func


def bind(f: Callable, x: Maybe[T]) -> Any:
    if isinstance(x, CheckError):
        return x
    return f(x)
