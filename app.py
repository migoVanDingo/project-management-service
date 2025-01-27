import uuid
from flask import Flask, g, jsonify, request, make_response
from flask_cors import CORS
import logging
from api.project.project_api import project_api
from utility.error import ThrowError



logging.basicConfig(filename='record.log',
                level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(lineno)d | \n %(message)-20s')

def create_app():
    app = Flask(__name__)
    CORS(app)

    #Register blueprints
    app.register_blueprint(project_api, url_prefix='/api')


    return app

app = create_app()


@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    else:
        request_id = str(uuid.uuid4())
        g.request_id = request_id


@app.errorhandler(ThrowError)
def handle_throw_error(error):
    response = jsonify({
        "message": str(error),
        "error_code": error.status_code
    })
    response.status_code = error.status_code
    return response