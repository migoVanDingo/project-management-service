from flask import Blueprint, current_app, g, json, request

from api.project.handler.request_create_project import RequestCreateProject
from api.project.handler.request_delete_project import RequestDeleteProject
from api.project.handler.request_get_project import RequestGetProject
from api.project.handler.request_get_project_list import RequestGetProjectList
from api.project.handler.request_update_project import RequestUpdateProject


project_api = Blueprint('project_api', __name__)

# Endpoint for CRUD project
@project_api.route('/project', methods=['POST'])
def create_project():
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    data = json.loads(request.data)
    api_request = RequestCreateProject(request_id, data)
    response = api_request.do_process()
    return response


@project_api.route('/project', methods=['GET'])
def read_project():
    args = request.args
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    api_request = RequestGetProject(request_id, args)
    response = api_request.do_process()
    return response


@project_api.route('/project/all', methods=['GET'])
def list_project():
    args = request.args
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    api_request = RequestGetProjectList(request_id, args)
    response = api_request.do_process()
    return response


@project_api.route('/project/<string:id>', methods=['PUT'])
def update_project(id):
    data = json.loads(request.data)
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    api_request = RequestUpdateProject(request_id, id, data)
    response = api_request.do_process()
    return response



@project_api.route('/project/<string:id>', methods=['DELETE'])
def delete_project(id):
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    api_request = RequestDeleteProject(request_id, id)
    response = api_request.do_process()
    return response

