from aiolambda.errors import ObjectAlreadyExists, ObjectNotFound
from aiolambda.typing import Maybe, Response

from auth.errors import InvalidPassword


def return_error(error: Exception) -> Response:
    if isinstance(error, ObjectNotFound):
        return ('Invalid credentials', 422)
    if isinstance(error, ObjectAlreadyExists):
        return ('User already exists', 409)
    if isinstance(error, InvalidPassword):
        return ('Invalid credentials', 422)
    return ('Unknow error', 500)


def return_200(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, Exception):
        return return_error(maybe_json)
    return ('', 200)


def return_201(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, Exception):
        return return_error(maybe_json)
    return (maybe_json, 201)


def return_204(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, Exception):
        return return_error(maybe_json)
    return ('', 204)
