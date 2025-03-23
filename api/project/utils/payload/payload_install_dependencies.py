class PayloadInstallDependencies:
    @staticmethod
    def form_payload(data: dict):
        payload = {
            "project_path": data.get("project_path")
        }

        return payload