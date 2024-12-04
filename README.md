# FunctionAppControl

A Python script to enable or disable an Azure Function App using Azure SDK for Python.

## Overview

This script interacts with Azure's `WebSiteManagementClient` to control the state (enable/disable) of a specific Azure Function App. It uses Azure Identity for authentication and requires an Azure subscription with the necessary permissions to manage the Function App.

## Prerequisites

Before using this script, ensure that you have the following:

1. **Azure Subscription**: You must have an Azure subscription ID with permissions to manage Azure Function Apps.
2. **Azure Function App**: The script is designed to manage an existing Function App within your Azure subscription.
3. **Azure CLI Login**: The script uses the `DefaultAzureCredential` for authentication, so you should be logged into Azure CLI, or use a Service Principal if running in an automated environment.

## Requirements

- Python 3.x
- `azure-identity` library
- `azure-mgmt-web` library

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

# Setup

## Step 1: Set Azure Subscription ID
Make sure to set your Azure subscription ID as an environment variable:

```bash
export AZURE_SUBSCRIPTION_ID="your-azure-subscription-id"
```

Replace "your-azure-subscription-id" with your actual Azure subscription ID. You can find this in the Azure portal under Subscriptions.

## Step 2: Modify the Script
In the python script, update the following parameters:

function_app_name: The name of your Azure Function App (e.g., "FunctionAppEnTest1").
resource_group_name: The name of the resource group where your Function App is located (e.g., "functionappentest").

```python
function_app_name = "FunctionAppEnTest1"  # Replace with your Function App name
resource_group_name = "functionappentest"  # Replace with your Resource Group name
```

## Step 3: Run the Script
Execute the script from the terminal:

```bash
python <script>.py
```

The script will print the current status of the Function App and ask you whether you want to enable or disable it.

## Step 4: User Input
Once the script runs, you will be prompted to either disable or enable the Function App. Enter:

d - to disable the Function App.
e  - to enable the Function App.

If the Function App is already in the desired state, the script will inform you that no changes are necessary.

```sql
Current status of 'FunctionAppEnTest1': Running
Do you want to disable (d) or enable (e) the Function App? (Enter 'd' or 'e'): d
FunctionAppEnTest1 has been disabled.
```
