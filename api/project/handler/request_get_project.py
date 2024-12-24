import traceback
from flask import current_app
from interface.abstract_handler import AbstractHandler
from utility.error import ThrowError


class RequestGetProject(AbstractHandler):
    def __init__(self, request_id: str, args: dict):
        self.request_id = request_id
        self.args = args

    def do_process(self):
        try:
            return "NOT_IMPLEMENTED"
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- Error getting project: {str(e)}")
            raise ThrowError("Error getting project", 500)