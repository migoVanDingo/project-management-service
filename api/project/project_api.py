from flask import Blueprint, current_app, g, json, request

from api.project.handler.request_clone_project import RequestCloneProject
from api.project.handler.request_configure_env import RequestConfigureEnv
from api.project.handler.request_create_project import RequestCreateProject
from api.project.handler.request_create_project_directory import RequestCreateProjectDirectory
from api.project.handler.request_delete_project import RequestDeleteProject
from api.project.handler.request_get_project import RequestGetProject
from api.project.handler.request_get_project_list import RequestGetProjectList
from api.project.handler.request_init_venv import RequestInitVenv
from api.project.handler.request_install_requirements import RequestInstallRequirements
from api.project.handler.request_job_clone_repo_project import RequestJobCloneRepoProject
from api.project.handler.request_update_project import RequestUpdateProject
from api.project.utils.payload.payload_configure_env import PayloadConfigureEnv
from api.project.utils.payload.payload_install_dependencies import PayloadInstallDependencies
from api.project.utils.payload.payload_clone_project import PayloadCloneProject
from api.project.utils.payload.payload_create_project_directory import PayloadCreateProjectDirectory
from api.project.utils.payload.payload_init_venv import PayloadInitVenv


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
    args = request.args.to_dict()
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    api_request = RequestGetProject(request_id, args)
    response = api_request.do_process()
    return response


@project_api.route('/project/all', methods=['GET'])
def list_project():
    args = request.args.to_dict()
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


@project_api.route('/project/clone', methods=['POST'])
def job_clone_project():
    request_id = g.request_id
    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- {request.url}")

    data = json.loads(request.data)
    api_request = RequestJobCloneRepoProject(request_id, data)
    response = api_request.do_process()
    return response



# JOB - CLONE REPO PROJECT
@project_api.route('/project/directory', methods=['POST'])
def create_project_directory():
    data = json.loads(request.data)
    if "request_id" in data:
        request_id = data['request_id']
    elif "job_id" in data:
        request_id = data['job_id']
    else:
        request_id = g.request_id

    api_request = RequestCreateProjectDirectory(request_id, PayloadCreateProjectDirectory.form_payload(data))
    response = api_request.do_process()

    if response["status"] == "SUCCESS":
        res_data = response["data"]
        res_data.update(data)
        return { "status": response["status"], "data": res_data}
    
    return response

@project_api.route('/project/clone', methods=['POST'])
def clone_project():
    data = json.loads(request.data)
    if "request_id" in data:
        request_id = data['request_id']
    elif "job_id" in data:
        request_id = data['job_id']
    else:
        request_id = g.request_id

    api_request = RequestCloneProject(request_id, PayloadCloneProject.form_payload(data))
    response = api_request.do_process()

    if response["status"] == "SUCCESS":
        res_data = response["data"]
        res_data.update(data)
        return { "status": response["status"], "data": res_data}
    
    return response


@project_api.route('/project/venv/init', methods=['POST'])
def init_venv():
    data = json.loads(request.data)
    if "request_id" in data:
        request_id = data['request_id']
    elif "job_id" in data:
        request_id = data['job_id']
    else:
        request_id = g.request_id

    current_app.logger.info(f"{request_id} --- {__name__} --- {request.method} --- init_venv DATA: {data}")

    api_request = RequestInitVenv(request_id, PayloadInitVenv.form_payload(data))
    response = api_request.do_process()

    if response["status"] == "SUCCESS":
        res_data = response["data"]
        res_data.update(data)
        return { "status": response["status"], "data": res_data}
    
    return response

@project_api.route('/project/requirements/install', methods=['POST'])
def install_requirements():
    data = json.loads(request.data)
    if "request_id" in data:
        request_id = data['request_id']
    elif "job_id" in data:
        request_id = data['job_id']
    else:
        request_id = g.request_id

    api_request = RequestInstallRequirements(request_id, PayloadInstallDependencies.form_payload(data))
    response = api_request.do_process()

    if response["status"] == "SUCCESS":
        res_data = response["data"]
        res_data.update(data)
        return { "status": response["status"], "data": res_data}
    
    return response

@project_api.route('/project/config/env', methods=['POST'])
def configure_variables():
    data = json.loads(request.data)
    if "request_id" in data:
        request_id = data['request_id']
    elif "job_id" in data:
        request_id = data['job_id']
    else:
        request_id = g.request_id

    api_request = RequestConfigureEnv(request_id, PayloadConfigureEnv.form_payload(data))
    response = api_request.do_process()

    if response["status"] == "SUCCESS":
        res_data = response["data"]
        res_data.update(data)
        return { "status": response["status"], "data": res_data}
    
    return response
