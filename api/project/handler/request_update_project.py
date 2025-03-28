import traceback
from flask import current_app
from interface.abstract_handler import AbstractHandler
from utility.error import ThrowError


class RequestUpdateProject(AbstractHandler):
    def __init__(self, request_id: str, project_id: str, payload: dict):
        self.request_id = request_id
        self.project_id = project_id
        self.payload = payload

    def do_process(self):
        try:
            return "NOT_IMPLEMENTED"
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- Error updating project: {str(e)}")
            raise ThrowError("Error updating project", 500)