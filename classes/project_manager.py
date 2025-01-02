import os
import traceback

from flask import current_app

from api.project.utils.directory_utils import DirUtils
from api.project.utils.git_utility import GitUtility
from api.project.utils.payload.project_payload import ProjectPayload
from utility.constant import Constant
from utility.error import ThrowError
from utility.request import Request


class ProjectManager:
    def __init__(self):
        pass

    def init_clone_project(self, request_id, project_id: str, git_url: str):
        try:
            # Create project directory
            project_dir = os.path.join(Constant.path_dir, project_id)
            full_path = DirUtils.create_directory(request_id, project_dir)

            

            # Clone project and get commit, url and branch
            gitUtil = GitUtility()
            clone_dir = gitUtil.clone(git_url, project_dir)

            current_app.logger.info(f"{request_id} --- {self.__class__.__name__} --- Clone directory: {clone_dir}")

            for dir in Constant.project_dir_tree:
                DirUtils.create_directory(request_id, os.path.join(project_dir, dir))

            # Get git info
            git_info = gitUtil.get_git_info(os.path.join(full_path, clone_dir))

            # Form project_git_info payload
            project_git_info_payload = ProjectPayload.form_save_project_git_info_payload({
                "project_id": project_id,
                "commit": git_info['current_commit'],
                "url": git_url,
                "branch": git_info["current_branch"]
            })


            # Insert project_git_info to database
            insert_project_git_info_request = Request()
            insert_project_git_info_response = insert_project_git_info_request.insert(request_id, Constant.table["PROJECT_GIT_INFO"], project_git_info_payload)

            current_app.logger.info(f"{request_id} --- {self.__class__.__name__} --- Insert project git info response: {insert_project_git_info_response}")

            return insert_project_git_info_response
        except Exception as e:
            current_app.logger.error(f"{request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- Error in cloning project: {str(e)}")
            raise ThrowError("Error in cloning project", 500)



