from functools import partial

from aiolambda.functools import _iscoroutinefunction_or_partial, compose, bind


def test_iscoroutinefunction_or_partial():
    async def foo(boo, woo):
        return (boo, woo)
    partial_foo = partial(foo, None)
    assert _iscoroutinefunction_or_partial(partial_foo) is True


def test_iscoroutinefunction_or_partial_false():
    def foo(boo, woo):
        return (boo, woo)
    partial_foo = partial(foo, None)
    assert _iscoroutinefunction_or_partial(partial_foo) is False


def test_compose():
    def x2(x: int) -> int:
        return x * 2

    def plus5(x: int) -> int:
        return x + 5
    assert compose(x2, plus5)(1) == 7
    assert compose(x2, plus5, x2)(1) == 14


async def test_compose_async():
    async def x2(x: int) -> int:
        return x * 2

    async def plus5(x: int) -> int:
        return x + 5
    assert await compose(x2, plus5)(1) == 7
    assert await compose(x2, plus5, x2)(1) == 14


def test_bind():
    def x5(x: int) -> int:
        return x * 5

    maybe_x5 = partial(bind, x5)
    assert maybe_x5(1) == 5

    exception = maybe_x5(Exception())
    assert isinstance(exception, Exception)
    assert not isinstance(exception, int)
