print("Hello from the woorld of python for Devops")

servers = [
    {"id": "srv-1", "status": "running", "env": "prod"},
    {"id": "srv-2", "status": "stopped", "env": "dev"},
    {"id": "srv-3", "status": "running", "env": "dev"},
]

for server in servers:
    if server["env"] == "dev":
        print(server["id"])