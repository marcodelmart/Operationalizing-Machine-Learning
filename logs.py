from azureml.core import Workspace
from azureml.core.webservice import Webservice

ws = Workspace.from_config()
name = "bankmarketing-model" # Updated with our deployment name

service = Webservice(name=name, workspace=ws)
logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
