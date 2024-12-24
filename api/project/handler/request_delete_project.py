import traceback
from flask import current_app
from interface.abstract_handler import AbstractHandler
from utility.error import ThrowError


class RequestDeleteProject(AbstractHandler):
    def __init__(self, request_id: str, project_id: str):
        self.request_id = request_id
        self.project_id = project_id

    def do_process(self):
        try:
            return "NOT_IMPLEMENTED"
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- Error deleting project: {str(e)}")
            raise ThrowError("Error deleting project", 500)
