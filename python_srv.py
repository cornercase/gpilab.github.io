#!/usr/bin/env python
# https://docs.python.org/2/library/simplehttpserver.html
#
# For checking how the docs render locally.
#   1. Run this in the docs directory.
#   2. Point your browser to http://localhost:8000

import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "\nServing @ http://localhost:"+str(PORT)+"\n"
httpd.serve_forever()
