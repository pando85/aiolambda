from aiohttp.web import Response, json_response

from aiolambda.typing import Maybe

from jwt.errors import JWTEncodeError


def return_error(error: Exception) -> Response:
    if isinstance(error, JWTEncodeError):
        return json_response('Error creating JWT', status=400)
    return json_response('Unknow error', status=500)


def return_200(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, Exception):
        return return_error(maybe_json)
    return json_response(maybe_json, status=200)


def return_201(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, Exception):
        return return_error(maybe_json)
    return json_response(maybe_json, status=201)


def return_204(maybe_json: Maybe[dict]) -> Response:
    if isinstance(maybe_json, Exception):
        return return_error(maybe_json)
    return json_response('', status=204)
