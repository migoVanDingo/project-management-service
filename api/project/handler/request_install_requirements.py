import os
import subprocess
from flask import current_app
from interface.abstract_handler import AbstractHandler


class RequestInstallRequirements(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(
                f"{self.request_id} --- {self.__class__.__name__} --- INSTALL REQUIREMENTS: {self.payload}")

            os.chdir(self.payload["project_path"])
            subprocess.run(["source", ".venv/bin/activate"])
            result = subprocess.run(
                ["pip", "install", "-r", "requirements.txt"],
                capture_output=True,
                text=True,
                check=True  # Raises a CalledProcessError if pip fails
            )

            current_app.logger.info(
                f"{self.request_id} --- {self.__class__.__name__} --- Requirements successfully installed")
            
            return {"status": "SUCCESS", "data": {}}
        except subprocess.CalledProcessError as e:
            # Extract only the error message
            error_message = e.stderr.strip().split("\n")[-1]  # Get the last line of stderr
            current_app.logger.error(
                f"{self.request_id} --- {self.__class__.__name__} --- {error_message}")
            return {"status": "FAILED", "error": error_message}

        except Exception as e:
            current_app.logger.error(
                f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}
