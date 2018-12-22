from typing import Dict

from auth.user import User
from aiolambda.functools import bind


@bind
def create_token(user: User) -> Dict[str, str]:
    print(user)
    return {'token': 'TODO'}
