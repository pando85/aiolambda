from aiohttp.web import Response
from typing import Optional


def return_response(_json: Optional[str]) -> Response:
    msg = _json
    status_code = 200
    if not _json:
        msg = '{"error": "Not quote found"}'
        status_code = 500
    return Response(body=msg, content_type='application/json', status=status_code)
