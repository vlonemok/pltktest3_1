from http.server import BaseHTTPRequestHandler
import urllib.parse as urlparse

def addtwonumbers():
    return  50

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/addtwonumbers?a=20&b=30":
            addtwonumbers()
            self.send_response(50)
        self.send_response(200)
        self.end_headers()
        return

if __name__ == '__main__':
    from http.server import HTTPServer

    server = HTTPServer(('', 9978), GetHandler)
    print('Starting server at http://localhost:9978')
    server.serve_forever()
