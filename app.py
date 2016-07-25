# 3rd-party
from bottle import run

# Local
import routes.routes

run(host='0.0.0.0', port=8080, debug=True, reloader=True)