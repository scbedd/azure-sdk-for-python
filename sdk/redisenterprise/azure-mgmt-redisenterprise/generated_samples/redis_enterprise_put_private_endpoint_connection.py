# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.redisenterprise import RedisEnterpriseManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-redisenterprise
# USAGE
    python redis_enterprise_put_private_endpoint_connection.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = RedisEnterpriseManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="e7b5a9d2-6b6a-4d2f-9143-20d9a10f5b8f",
    )

    response = client.private_endpoint_connections.begin_put(
        resource_group_name="rg1",
        cluster_name="cache1",
        private_endpoint_connection_name="pectest01",
        properties={
            "properties": {"privateLinkServiceConnectionState": {"description": "Auto-Approved", "status": "Approved"}}
        },
    ).result()
    print(response)


# x-ms-original-file: specification/redisenterprise/resource-manager/Microsoft.Cache/preview/2024-09-01-preview/examples/RedisEnterprisePutPrivateEndpointConnection.json
if __name__ == "__main__":
    main()
