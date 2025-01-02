import os
import subprocess
import traceback

from flask import current_app
from git import Repo

from utility.constant import Constant

class GitUtility:
    def __init__(self)->None:
        pass

    def git_init(self, path:str)->str:
        try:
            
            os.chdir(path)
            subprocess.run(['git', 'init'])
            subprocess.run(['dvc', 'init'])
            return "success"
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} --- {traceback.format_exc()} :: Error initializing git :: path: {path} :: {str(e)}")
            return str(e)
        

    def clone(self, url: str, project_dir: str) -> str:
        try:
        
            os.chdir(os.path.join(Constant.project_root_dir, project_dir))
            subprocess.run(['git', 'clone', url])
            current_app.logger.debug(f"{self.__class__.__name__} :: Cloning project :: url: {url} :: project_dir: {project_dir}")

            dir = os.listdir(os.path.join(Constant.project_root_dir, project_dir))

            return dir[0]
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} --- {traceback.format_exc()} :: Error cloning project :: url: {url} :: project_dir: {project_dir} :: {str(e)}")
            return str(e)
        
    def sync_project(self, project_id: str, dir_name: str) -> None:
        try:
            os.chdir(os.path.join(os.environ["PROJECT_ROOT"],project_id, "project", dir_name))
            subprocess.run(['git', 'fetch'])
            subprocess.run(['git', 'pull'])
            current_app.logger.debug(f"{self.__class__.__name__} :: Syncing project :: project_id: {project_id}")

            return "project_SYNCED"
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} --- {traceback.format_exc()} :: Error syncing project :: project_id: {project_id} :: {str(e)}")
            return str(e)
        

    def get_git_info(self, repo_path: str):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: Getting git info :: repo_path: {repo_path}")
            repo = Repo(repo_path)
            current_commit = repo.head.commit.hexsha
            current_branch = repo.active_branch.name
            branch_names = [branch.name for branch in repo.branches]
            
            return {
                "current_commit": current_commit,
                "current_branch": current_branch,
                "branches": branch_names
            }
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} --- {traceback.format_exc()} :: Error getting git info :: repo_path: {repo_path} :: {str(e)}")
            return str(e)

