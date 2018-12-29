import inspect

from toolz import curry

import aiolambda.errors
from aiolambda.functools import compose


def test_all_errors_are_exceptions():
    assert compose(
        curry(filter)(lambda x: inspect.isclass(x)),
        curry(map)(lambda _cls: isinstance(_cls(), Exception)),
        all
    )(aiolambda.errors.__dict__.values())
