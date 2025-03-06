from flask import current_app
import requests
from api.project.utils.payload.payload_job_clone_repo_project import PayloadJobCloneRepoProject
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant


class RequestJobCloneRepoProject(AbstractHandler):

    """
        Class: Create a job to clone a repo project. Send to job service for delegation.
    """

    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- CREATE JOB CLONE REPO PROJECT")
            
            data = PayloadJobCloneRepoProject.form_job_payload(self.payload)
            response = requests.post(Constant.base_url + Constant.services["JOB"]["PORT"] + Constant.services["JOB"]["ENDPOINT"]["CREATE-JOB"], json=data)

            print(f"Response: {response}")
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Response: {response.json()}")
            response = response.json()

            if "status" not in response:
                current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- Job creation failed")
                raise Exception(f"{self.request_id} --- {self.__class__.__name__} --- Job creation failed. Repo not cloned within this project")

            return {"status": "SUCCESS", "data": response['job_id']}

    
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}