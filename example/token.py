from functools import partial

from example.user import User
from aiolambda.typing import Maybe, Success
from aiolambda.functools import bind


def _create_token(user: User) -> Maybe[Success]:
    print(user)
    return Success({'token': 'TODO'}, 200)


create_token = partial(bind, _create_token)
