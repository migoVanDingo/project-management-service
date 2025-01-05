import os
import traceback
from flask import current_app
from api.project.utils.directory_utils import DirUtils
from api.project.utils.git_utility import GitUtility
from api.project.utils.payload.project_payload import ProjectPayload
from classes.project_manager import ProjectManager
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant
from utility.error import ThrowError
from utility.request import Request


class RequestCreateProject(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            # Log payload
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Payload: {self.payload}")

            # Insert project to database
            insert_project_request = Request()
            insert_project_response = insert_project_request.insert(self.request_id, Constant.table["PROJECT"], ProjectPayload.form_save_project_payload(self.payload))

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Insert project response: {insert_project_response['response']}")

            # Use project_id to update the path
            project_id = insert_project_response["response"]["project_id"]
            path = os.path.join(Constant.path_dir, project_id)
            update_project_request = Request()
            update_project_request.update(self.request_id, Constant.table["PROJECT"], "project_id", project_id, {"path": path})
            insert_project_response["response"]["path"] = path

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Update project path response: {insert_project_response['response']}")

            # If clone_project, clone project
            ## Insert clone_project to database
            if "clone_project" in self.payload and self.payload["clone_project"] is not None:

                current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Cloning project: {self.payload['git_url']}")
                project_manager = ProjectManager()
                project = project_manager.init_clone_project(self.request_id, insert_project_response["response"]["project_id"], self.payload["git_url"])
                insert_project_response["response"]["git_info"] = project   

                  

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Create project complete: {insert_project_response['response']}")
            return insert_project_response["response"]

          
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- Error in creating project: {str(e)}")
            raise ThrowError("Error in creating project", 500)

