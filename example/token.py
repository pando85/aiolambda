from functools import partial
from typing import Dict

from example.user import User
from aiolambda.functools import bind


def _create_token(user: User) -> Dict[str, str]:
    print(user)
    return {'token': 'TODO'}


create_token = partial(bind, _create_token)
