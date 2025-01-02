import os
import traceback

from flask import current_app

from utility.constant import Constant


class DirUtils:
    @staticmethod
    def create_directory(request_id, path):
        try:
            full_path = os.path.join(Constant.project_root_dir, path)
            os.makedirs(full_path, exist_ok=True)
            return full_path
        except Exception as e:
            current_app.logger.error(f"{request_id} --- {__class__.__name__} --- {traceback.format_exc()} --- {e}")
            return False