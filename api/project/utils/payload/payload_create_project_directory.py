class PayloadCreateProjectDirectory:
    @staticmethod
    def form_payload(data: dict):
        payload = {
            "project_id": data.get("project_id"),
            "user_id": data.get("user_id")
        }

        return payload