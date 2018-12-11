from aiohttp.web import Response, json_response

from aiolambda.errors import ObjectAlreadyExists, ObjectNotFound

from example.errors import InvalidPassword
from example.typing import CheckError, Error, Maybe


def return_error(error: Error) -> Response:
    if isinstance(error, ObjectNotFound):
        return json_response('Invalid credentials', status=422)
    if isinstance(error, ObjectAlreadyExists):
        return json_response('User already exists', status=409)
    if isinstance(error, InvalidPassword):
        return json_response('Invalid credentials', status=422)
    return json_response('Unknow error', status=500)


def return_200(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, CheckError):
        return return_error(maybe_json)
    return json_response('', status=200)


def return_201(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, CheckError):
        return return_error(maybe_json)
    return json_response(maybe_json, status=201)


def return_204(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, CheckError):
        return return_error(maybe_json)
    return json_response('', status=204)
