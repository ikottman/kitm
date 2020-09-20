import os
import datetime
import json
import http.server
import socketserver
from http import HTTPStatus
from urllib.request import Request, urlopen
from urllib.error import HTTPError

def log(request, response):
    message = {
        'timestamp': str(datetime.datetime.now()),
        'request': request,
        'response': response
    }
    print(json.dumps(message, indent=2))

def call(url, headers, method, data=None):
    req = Request(url, data=data)
    for header in headers:
        req.add_header(header, headers.get(header))

    try:
        return urlopen(req)
    except HTTPError as e:
        return e
    return None

def request_log(verb, url, headers):
    return {
        'method': verb,
        'url': url,
        'headers': [{ header: headers.get(header) } for header in headers]
    }

def is_json(val):
  try:
    json.loads(val)
  except:
    return False
  return True

def response_log(response):
    body = response.read() or None

    if is_json(body):
        body = json.loads(body)
    else:
        body = str(body)

    return {
        'status': response.code,
        'body': body,
        'headers': [{ header: response.headers.get(header) } for header in response.headers]
    }

def build_url(path):
    return 'http://host.docker.internal:' + os.environ['PORT'] + path

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = build_url(self.path)
        response = call(url, self.headers, 'GET')
        log(request_log('GET', url, self.headers), response_log(response))

        self.send_response(response.code)
        self.end_headers()
        self.wfile.write(response.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        url = build_url(self.path)
        response = call(url, self.headers, 'POST', body)
        log(request_log('POST', url, self.headers), response_log(response))

        self.send_response(response.code)
        self.end_headers()
        self.wfile.write(response.read())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        url = build_url(self.path)
        response = call(url, self.headers, 'POST', body)
        log(request_log('POST', url, self.headers), response_log(response))

        self.send_response(response.code)
        self.end_headers()
        self.wfile.write(response.read())

    def log_message(self, format, *args):
        # disable built in access logs
        return

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()