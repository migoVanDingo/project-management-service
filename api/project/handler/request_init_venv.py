import os
import subprocess
from flask import current_app
from interface.abstract_handler import AbstractHandler
from utility.request import Request


class RequestInitVenv(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- INIT VENV: {self.payload}")

            dao_request = Request()
            project_response = dao_request.read(self.request_id, "project_version", {"project_version_id": self.payload["project_version_id"]})

            if project_response is None or "response" not in project_response:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Project version not found")
                raise Exception(f"Project version not found")
            
            if project_response["response"]["is_venv"] == 1:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Venv already initialized")
                return {"status": "SUCCESS", "data": {}}

            os.chdir(self.payload["project_path"])
            subprocess.run(["python3", "-m", "venv", ".venv"])

            update_project_version = dao_request.update(self.request_id, "project_version", {"is_venv": 1}, {"project_version_id": self.payload["project_version_id"]})

            if "response" not in update_project_version:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Project version not updated")
                raise Exception(f"Project version not updated")
            
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Venv initialized")
            return {"status": "SUCCESS", "data": {}}

        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}