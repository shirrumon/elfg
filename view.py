from elfg.view import View
from datetime import datetime
from elfg.request import Request
from elfg.response import Response
from elfg.template_engine import build_template


class Homepage(View):
    def get(self, request: Request, *args, **kwargs):
        body = build_template(request, {'time': str(datetime.now()), 'lst': [1, 2, 5, 23], 'session_id': request.session_id}, 'home.html')
        return Response(request, body=body)


class EpicMath(View):
    def get(self, request: Request, *args, **kwargs):
        first = request.GET.get('first')
        if not first or not first[0].isnumeric():
            return Response(request, body=f'first is empty or not a number')

        second = request.GET.get('second')
        if not second or not second[0].isnumeric():
            return Response(request, body=f'second is empty or not a number')

        return Response(request, body=f'Sum {first[0]} and {second[0]} is: {int(first[0]) + int(second[0])}')


class Hello(View):
    def get(self, request: Request, *args, **kwargs) -> Response:
        body = build_template(request, {'name': 'unknown'}, 'hello.html')
        return Response(request, body=body)

    def post(self, request: Request, *args, **kwargs) -> Response:
        raw_name = request.POST.get('answer')
        name = raw_name[0] if raw_name else 'unknown'
        body = build_template(request, {'name': name}, 'hello.html')
        return Response(request, body=body)
