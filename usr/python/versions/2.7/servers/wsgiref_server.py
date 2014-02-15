import os
from wsgiref.simple_server import make_server

import app


server = make_server(os.environ["OPENSHIFT_ADVANCED_PYTHON_IP"], 15000, app.application)
print "Serving HTTP on port 15000..."

server.serve_forever()