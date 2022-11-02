from flask import Flask
from flask.logging import create_logger
from logging.config import dictConfig
from base64 import b64decode
from json import dumps
from werkzeug.exceptions import BadRequest, Unauthorized, Conflict, ServiceUnavailable
from utils.environment import load_environment, get_environment
from flask_cors import CORS

#
#   Create app and load ENV
#
load_environment("ssl/config-db-json")
serverConfig = get_environment("Server")
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s: %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
app = Flask(__name__)
CORS(app)
app.config['SESSION_COOKIE_NAME'] = serverConfig['SessionName']
app.config['MONGO_URI'] = get_environment("Mongo")
app.secret_key = b64decode(serverConfig['Secret']) 
rooturl = serverConfig['AppRoot']

logger = create_logger(app)
logger.info(f"ENV_MODE: {serverConfig['EnvMode']}")
logger.info(f"ROOT: {rooturl}")
logger.info(f"SESSION: {app.config['SESSION_COOKIE_NAME']}")

type_response = "application/json"

################################
#                              #
# Begin Register Controllers   #
#                              #
################################

from model.puesto import prueba_data
app.register_blueprint(prueba_data, url_prefix=rooturl)

from controller.apiUsuario import api_usuario
app.register_blueprint(api_usuario, url_prefix=rooturl)

from controller.apiBono import api_bono
app.register_blueprint(api_bono, url_prefix=rooturl)

from controller.apiDescuento import api_descuento
app.register_blueprint(api_descuento, url_prefix=rooturl)

from controller.apiFamiliar import api_familiar
app.register_blueprint(api_familiar, url_prefix=rooturl)

from controller.apiHoraExtra import api_hora_extra
app.register_blueprint(api_hora_extra, url_prefix=rooturl)

from controller.apiPuesto import api_puesto
app.register_blueprint(api_puesto, url_prefix=rooturl)

from controller.apiPlanilla import api_planilla
app.register_blueprint(api_planilla, url_prefix=rooturl)

from controller.apiEmpleado import api_empleado
app.register_blueprint(api_empleado, url_prefix=rooturl)

from controller.apiDetallePlanilla import api_detalle_planilla
app.register_blueprint(api_detalle_planilla, url_prefix=rooturl)
##############################
#                            #
# End Register Controllers   #
#                            #
##############################

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = dumps({
        "status": "Error",
        "detalle": e.name,
        "data": {},
    })
    response.content_type = type_response
    return response

@app.errorhandler(Unauthorized)
def handle_unauthorized(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = dumps({
        "status": "Error",
        "detalle": e.name,
        "data": {},
    })
    response.content_type = type_response
    return response

@app.errorhandler(Conflict)
def handle_conflict(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = dumps({
        "status": "Error",
        "detalle": e.name,
        "data": {},
    })
    response.content_type = type_response
    return response


@app.errorhandler(ServiceUnavailable)
def handle_service_unavailable(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = dumps({
        "status": "Error",
        "detalle": e.name,
        "data": {},
    })
    response.content_type = type_response
    return response
class App:
    def get_app():
        return app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443, ssl_context='adhoc')