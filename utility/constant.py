class Constant:
    service = "project-management-service"

    project_root_dir = "/Users/bubz/Developer/master-project/tests/test-projects-root"
    path_dir = "projects"

    base_url = "http://localhost:"
    dao_port = "5010"

    project_dir_tree = [             # Git folder
        'pipelines',            # Stores pipeline definitions
        'params',               # Stores parameter files
        'output',               # Top-level directory for outputs
        'datasets',             # Optional for datasets
        'logs',                 # Logs directory
        'other_repo_files',     # For other repo files
    ]

    dao = {
        "create": "/api/create",
        "read": "/api/read",
        "list": "/api/read_list",
        "update": "/api/update",
        "delete": "/api/delete"
    }

    table = {
        "PROJECT": "project",
        "PROJECT_GIT_INFO": "project_git_info",
    }

    delimeter = {
        "PROJECT": "__"
    }

   
