import time


def current_timestamp() -> int:
    return int(time.time())


def get_secret(request) -> dict:
    return {
        'user_id': request['user'],
        'secret': 'wbevuec',
        'token_info': request['token_info']
    }
