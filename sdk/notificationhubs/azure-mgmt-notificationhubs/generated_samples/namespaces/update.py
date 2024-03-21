# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.notificationhubs import NotificationHubsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-notificationhubs
# USAGE
    python update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NotificationHubsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="29cfa613-cbbc-4512-b1d6-1b3a92c7fa40",
    )

    response = client.namespaces.update(
        resource_group_name="5ktrial",
        namespace_name="nh-sdk-ns",
        parameters={
            "properties": {
                "pnsCredentials": {
                    "gcmCredential": {
                        "properties": {
                            "gcmEndpoint": "https://fcm.googleapis.com/fcm/send",
                            "googleApiKey": "#############################",
                        }
                    }
                }
            },
            "sku": {"name": "Free"},
            "tags": {"tag1": "value3"},
        },
    )
    print(response)


# x-ms-original-file: specification/notificationhubs/resource-manager/Microsoft.NotificationHubs/preview/2023-10-01-preview/examples/Namespaces/Update.json
if __name__ == "__main__":
    main()
