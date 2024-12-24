from flask import Blueprint


project_api = Blueprint('project_api', __name__)

# Endpoint for CRUD project
@project_api.route('/project', methods=['POST'])
def create_project():
    pass

@project_api.route('/project', methods=['GET'])
def read_project():
    pass

@project_api.route('/project/all', methods=['GET'])
def list_project():
    pass

@project_api.route('/project', methods=['PUT'])
def update_project():
    pass

@project_api.route('/project', methods=['DELETE'])
def delete_project():
    pass

