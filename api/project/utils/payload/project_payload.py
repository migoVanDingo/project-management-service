from typing import List, Optional
from pydantic import BaseModel


class IInsertProject(BaseModel):
    name: str
    description: Optional[str] = ""
    path: Optional[str] = ""
    created_by: str
    entity_id: str
    entity_type: str

    
class IInsertProjectRole(BaseModel):
    project_id: str
    user_id: str
    role: List[str]
    level: int

    

class IInsertProjectGitInfo(BaseModel):
    project_id: str
    commit: str
    url: str
    branch: str


class ProjectPayload:

    @staticmethod
    def form_save_project_payload(data: dict) -> IInsertProject:

        payload = {
            "name": data.get("name"),
            "description": data.get("description"),
            "path": data.get("path"),
            "created_by": data.get("user_id"),
            "entity_id": data.get("entity_id"),
            "entity_type": data.get("entity_type")

        }
        return payload
    
    @staticmethod
    def form_save_project_role_payload(data: dict) -> IInsertProjectRole:
        payload = {
            "project_id": data.get("project_id"),
            "user_id": data.get("user_id"),
            "role": data.get("role"),
            "level": data.get("level")
        }

        return payload
    
    @staticmethod
    def form_save_project_git_info_payload(data: dict) -> IInsertProjectGitInfo:
        payload = {
            "project_id": data.get("project_id"),
            "latest_commit_hash": data.get("commit"),
            "git_clone_link": data.get("url"),
            "branch": data.get("branch")
        }
        return payload
