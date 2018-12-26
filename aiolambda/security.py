import six

from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem
from werkzeug.exceptions import Unauthorized
from jose import JWTError, jwt

from aiolambda.config import JWT_PUBLIC_KEY, JWT_ALGORITHM


def decode_token(token, required_scopes=None):
    try:
        info = jwt.decode(token, JWT_PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)

    if required_scopes is not None and not validate_scope(required_scopes, info['scope']):
        raise OAuthScopeProblem(
                description='Provided user doesn\'t have the required access rights',
                required_scopes=required_scopes,
                token_scopes=info['scope']
            )

    return info
