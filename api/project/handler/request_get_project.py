import traceback
from flask import current_app
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant
from utility.error import ThrowError
from utility.request import Request


class RequestGetProject(AbstractHandler):
    def __init__(self, request_id: str, args: dict):
        self.request_id = request_id
        self.args = args

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Args: {self.args}")
            dao_request = Request()
            response = dao_request.read(self.request_id, Constant.table["PROJECT"], self.args)
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Response: {response}")
            return response['response']
        
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- Error getting project: {str(e)}")
            raise ThrowError("Error getting project", 500)