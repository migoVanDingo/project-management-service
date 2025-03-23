class PayloadCloneProject:

    @staticmethod
    def form_payload(data: dict):
        payload = {
            "project_directory_path": data.get("project_directory_path"),
            "user_id": data.get("user_id"),
            "new_project_name": data.get("new_project_name"),
            "git_url": data.get("git_url")
        }

        return payload