from flask import current_app
from interface.abstract_handler import AbstractHandler


class RequestConfigureEnv(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- CONFIGURE VARIABLES: ******* NOT_IMPLEMENTED *******")


            return {"status": "SUCCESS", "data": {}}
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}