class PayloadInitVenv:
    @staticmethod
    def form_payload(data: dict):
        payload = {
            "project_version_id": data.get("project_version_id"),
            "project_path": data.get("project_path")
        }

        return payload
