# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.appcontainers import ContainerAppsAPIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python container_apps_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.container_apps.begin_create_or_update(
        resource_group_name="rg",
        container_app_name="testcontainerApp0",
        container_app_envelope={
            "location": "East US",
            "properties": {
                "configuration": {
                    "dapr": {
                        "appPort": 3000,
                        "appProtocol": "http",
                        "enableApiLogging": True,
                        "enabled": True,
                        "httpMaxRequestSize": 10,
                        "httpReadBufferSize": 30,
                        "logLevel": "debug",
                    },
                    "ingress": {
                        "clientCertificateMode": "accept",
                        "corsPolicy": {
                            "allowCredentials": True,
                            "allowedHeaders": ["HEADER1", "HEADER2"],
                            "allowedMethods": ["GET", "POST"],
                            "allowedOrigins": ["https://a.test.com", "https://b.test.com"],
                            "exposeHeaders": ["HEADER3", "HEADER4"],
                            "maxAge": 1234,
                        },
                        "customDomains": [
                            {
                                "bindingType": "SniEnabled",
                                "certificateId": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/rg/providers/Microsoft.App/managedEnvironments/demokube/certificates/my-certificate-for-my-name-dot-com",
                                "name": "www.my-name.com",
                            },
                            {
                                "bindingType": "SniEnabled",
                                "certificateId": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/rg/providers/Microsoft.App/managedEnvironments/demokube/certificates/my-certificate-for-my-other-name-dot-com",
                                "name": "www.my-other-name.com",
                            },
                        ],
                        "external": True,
                        "ipSecurityRestrictions": [
                            {
                                "action": "Allow",
                                "description": "Allowing all IP's within the subnet below to access containerapp",
                                "ipAddressRange": "192.168.1.1/32",
                                "name": "Allow work IP A subnet",
                            },
                            {
                                "action": "Allow",
                                "description": "Allowing all IP's within the subnet below to access containerapp",
                                "ipAddressRange": "192.168.1.1/8",
                                "name": "Allow work IP B subnet",
                            },
                        ],
                        "stickySessions": {"affinity": "sticky"},
                        "targetPort": 3000,
                        "traffic": [{"label": "production", "revisionName": "testcontainerApp0-ab1234", "weight": 100}],
                    },
                    "maxInactiveRevisions": 10,
                },
                "environmentId": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/rg/providers/Microsoft.App/managedEnvironments/demokube",
                "template": {
                    "containers": [
                        {
                            "image": "repo/testcontainerApp0:v1",
                            "name": "testcontainerApp0",
                            "probes": [
                                {
                                    "httpGet": {
                                        "httpHeaders": [{"name": "Custom-Header", "value": "Awesome"}],
                                        "path": "/health",
                                        "port": 8080,
                                    },
                                    "initialDelaySeconds": 3,
                                    "periodSeconds": 3,
                                    "type": "Liveness",
                                }
                            ],
                        }
                    ],
                    "initContainers": [
                        {
                            "args": ["-c", "while true; do echo hello; sleep 10;done"],
                            "command": ["/bin/sh"],
                            "image": "repo/testcontainerApp0:v4",
                            "name": "testinitcontainerApp0",
                            "resources": {"cpu": 0.2, "memory": "100Mi"},
                        }
                    ],
                    "scale": {
                        "maxReplicas": 5,
                        "minReplicas": 1,
                        "rules": [
                            {
                                "custom": {"metadata": {"concurrentRequests": "50"}, "type": "http"},
                                "name": "httpscalingrule",
                            }
                        ],
                    },
                },
                "workloadProfileName": "My-GP-01",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2022-11-01-preview/examples/ContainerApps_CreateOrUpdate.json
if __name__ == "__main__":
    main()
