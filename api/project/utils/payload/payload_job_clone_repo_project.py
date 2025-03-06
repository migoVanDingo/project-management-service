class PayloadJobCloneRepoProject:
    @staticmethod
    def form_job_payload(data: dict):
        payload = {
            "github_id": data.get("github_id"),
            "project_id": data.get("project_id"),
            "clone_url": data.get("clone_url"),
            "user_id": data.get("user_id"),
            "created_by": data.get("user_id"),
            "job_name": "CLONE_REPO_PROJECT"
        }

        return payload