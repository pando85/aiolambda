from jose import jwt

from aiolambda.config import JWT_ALGORITHM, JWT_ISSUER, JWT_LIFETIME_SECONDS, JWT_PRIVATE_KEY
from aiolambda.typing import Maybe

from jwt.utils import current_timestamp
from jwt.errors import JWTEncodeError


def generate_token(user_id: str) -> Maybe[dict]:
    timestamp = current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }

    try:
        return jwt.encode(payload, JWT_PRIVATE_KEY, algorithm=JWT_ALGORITHM)
    except Exception:
        return JWTEncodeError()
