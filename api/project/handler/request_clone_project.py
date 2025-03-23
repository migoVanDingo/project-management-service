import os
import subprocess
from flask import current_app
import git
from api.project.utils.payload.project_payload import ProjectPayload
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant
from utility.request import Request


class RequestCloneProject(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- CREATE JOB CLONE REPO PROJECT payload: {self.payload}")

            clone_path = os.path.join(Constant.project_root_dir, self.payload["project_directory_path"])

            if not os.path.exists(clone_path):
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Project directory not found")
                raise Exception(f"Clone project failed. Project directory not found")
            
            os.chdir(clone_path)
            subprocess.run(["git", "clone", self.payload["git_url"]])

            clone_dir = os.listdir(clone_path)[0]

            clone_path = os.path.join(clone_path, clone_dir)
            repo = git.Repo(clone_path)
            commit_hash = repo.head.object.hexsha
            current_branch = repo.active_branch.name

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- repo.head.object: {repo.head.object}")

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- active branch: {repo.active_branch}")

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Clone project complete : {clone_path}/{clone_dir}")

            # Insert into Project Version table

            payload_project_version = ProjectPayload.form_save_project_version_payload({
                **self.payload,
                "commit_hash": commit_hash,
                "branch": current_branch,
                "path": clone_path
            })

            dao_request = Request()
            insert_project_version_response = dao_request.insert(self.request_id, Constant.table["PROJECT_VERSION"], payload_project_version)

            if "response" not in insert_project_version_response:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Project version not inserted")
                raise Exception(f"Project version could not be created: {insert_project_version_response}")
            
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Project version inserted: {insert_project_version_response['response']}")

            return {"status": "SUCCESS", "data": {"project_path": insert_project_version_response["response"]["path"], "project_version_id": insert_project_version_response["response"]["project_version_id"]}}

            

        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}