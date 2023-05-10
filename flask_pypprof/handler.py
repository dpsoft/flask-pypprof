from io import BytesIO

from pypprof.net_http import PProfRequestHandler


class ProfileRequestHandler(PProfRequestHandler):
    def __init__(self, req):
        self.query = req.args
        self.wfile = HttpResponse(BytesIO())

    def send_response(self, code, message=None):
        self.wfile.status_code = code
        self.wfile.status = message

    def send_error(self, code, message=None, explain=None):
        self.wfile.status_code = code
        self.wfile.status = message

    def send_header(self, keyword, value):
        self.wfile.headers[keyword] = value
        # self.wfile[keyword] = value

    def end_headers(self) -> None:
        pass

    def profile(self):
        super().profile(self.query)

    def wall(self):
        super().wall(self.query)

    def heap(self):
        super().heap(self.query)

    def thread(self):
        super().thread(self.query)

    def get_response(self):
        return self.wfile


class HttpResponse:
    def __init__(self, content=b'', status=200, headers=None):
        self.status = status
        self.headers = headers or {}
        self.content = content

    def __bytes__(self):
        return self.content

    def __iter__(self):
        yield bytes(self)

    def write(self, content):
        self.content = content
