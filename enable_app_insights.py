from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Load workspace from config
ws = Workspace.from_config()

# The name of your deployed web service
name = "bankmarketing-model" 

# Load existing web service and update it to enable App Insights
service = Webservice(name=name, workspace=ws)
service.update(enable_app_insights=True)

print("Application Insights has been successfully enabled!")
