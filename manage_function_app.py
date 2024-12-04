import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient

# Parameters
function_app_name = "FunctionAppEnTest1"
resource_group_name = "functionappentest"

# Authenticate using Azure Identity
credential = DefaultAzureCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
client = WebSiteManagementClient(credential, subscription_id)

# Function to disable the Function App
def disable_function_app(app_name, resource_group):
    client.web_apps.stop(resource_group, app_name)
    print(f"{app_name} has been disabled.")

# Function to enable the Function App
def enable_function_app(app_name, resource_group):
    client.web_apps.start(resource_group, app_name)
    print(f"{app_name} has been enabled.")

# Get current status
try:
    current_function_app = client.web_apps.get(resource_group_name, function_app_name)
except Exception as e:
    print(f"Function App '{function_app_name}' not found in resource group '{resource_group_name}'.")
    exit()

current_status = current_function_app.state
print(f"Current status of '{function_app_name}': {current_status}")

# User input to disable or enable
user_input = input("Do you want to disable (d) or enable (e) the Function App? (Enter 'd' or 'e'): ")

if user_input.lower() == 'd':
    if current_status == "Running":
        disable_function_app(function_app_name, resource_group_name)
    else:
        print(f"{function_app_name} is already disabled.")
elif user_input.lower() == 'e':
    if current_status != "Running":
        enable_function_app(function_app_name, resource_group_name)
    else:
        print(f"{function_app_name} is already enabled.")
else:
    print("Invalid input. Please enter 'd' to disable or 'e' to enable.")
