# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerservice
# USAGE
    python maintenance_configurations_create_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerServiceClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid1",
    )

    response = client.maintenance_configurations.create_or_update(
        resource_group_name="rg1",
        resource_name="clustername1",
        config_name="default",
        parameters={
            "properties": {
                "notAllowedTime": [{"end": "2020-11-30T12:00:00Z", "start": "2020-11-26T03:00:00Z"}],
                "timeInWeek": [{"day": "Monday", "hourSlots": [1, 2]}],
            }
        },
    )
    print(response)


# x-ms-original-file: specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2023-01-01/examples/MaintenanceConfigurationsCreate_Update.json
if __name__ == "__main__":
    main()
