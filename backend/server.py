'''SOURCE: https://docs.python.org/3/library/http.server.html
HOW TO: spec different dir to serve files'''

import http.server
import socketserver
import os

PORT = 8000
FILE = os.path.dirname(__file__)
frontend_dir = os.path.join(FILE, '../frontend')
os.chdir(frontend_dir)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serve at port", PORT)
    httpd.serve_forever()