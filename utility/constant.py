class Constant:
    service = "project-management-service"

    datastore_root_dir = "/Users/bubz/Developer/master-project/tests/test-datastore-root"

    base_url = "http://localhost:"
    dao_port = "5013"

    dao = {
        "create": "/api/create",
        "read": "/api/read",
        "list": "/api/read_list",
        "update": "/api/update",
        "delete": "/api/delete"
    }

    table = {
        "DATASTORE": "datastore",
        "DATASET": "dataset",
        "FILES": "files",
        "PROJECT": "project",
    }

    delimeter = {
        "DATASTORE": "__",
        "DATASET": "__"
    }

   
