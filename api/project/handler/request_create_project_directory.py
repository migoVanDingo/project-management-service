import os
from flask import current_app
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant
from utility.request import Request


class RequestCreateProjectDirectory(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- CREATE PROJECT DIRECTORY: {self.payload}")

            if "project_id" not in self.payload or self.payload['project_id'] is None:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Project ID not in payload")
                raise Exception(f"Project ID not in payload")

            # Get project
            dao_request = Request()
            project_response = dao_request.read(self.request_id, Constant.table["PROJECT"], {"project_id": self.payload["project_id"]})

            if project_response is None or "response" not in project_response:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Project not found")
                raise Exception(f"Project not found")
            

            project_directory = os.path.join(Constant.user_dir, self.payload["user_id"], Constant.path_dir, self.payload["project_id"])
            path = os.path.join(Constant.project_root_dir, project_directory)

            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
                current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Project directory created: {path}")

            return {"status": "SUCCESS", "data": {"project_directory_path": project_directory}}


        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}