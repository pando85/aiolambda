import aiohttp.web
import six

from connexion.decorators.security import validate_scope as connexion_validate_scope
from werkzeug.exceptions import Unauthorized
from jose import JWTError, jwt

from aiolambda.config import JWT_PUBLIC_KEY, JWT_ALGORITHM


def decode_token(token, required_scopes=None):
    try:
        info = jwt.decode(token, JWT_PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)
    return info


def validate_scope(required_scopes, token_scopes):
    is_valid = connexion_validate_scope(required_scopes, token_scopes)
    if not is_valid:
        raise aiohttp.web.HTTPForbidden
    return is_valid
