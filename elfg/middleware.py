from elfg.request import Request
from elfg.response import Response
from uuid import uuid4
from urllib.parse import parse_qs


class BaseMidlleware:
    def to_request(self, request: Request):
        return

    def to_response(self, response: Response):
        return

class Session(BaseMidlleware):
    def to_request(self, request: Request):
        cookie = request.environ.get('HTTP_COOKIE', None)
        if not cookie:
            return
        session_id = parse_qs(cookie)['session_id'][0]
        request.extra['session_id'] = session_id



    def to_response(self, response: Response):
        if not response.request.session_id:
            response.update_headers(
                {'Set-Cookie': f'session_id={uuid4()}'}
            )

middlewares = [

]