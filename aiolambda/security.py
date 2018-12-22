import six
from werkzeug.exceptions import Unauthorized
from jose import JWTError, jwt


from aiolambda.config import JWT_PUBLIC_KEY, JWT_ALGORITHM


def decode_token(token):
    try:
        return jwt.decode(token, JWT_PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)
