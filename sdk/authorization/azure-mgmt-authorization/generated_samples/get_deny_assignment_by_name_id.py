# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-authorization
# USAGE
    python get_deny_assignment_by_name_id.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AuthorizationManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.deny_assignments.get(
        scope="subscriptions/subId/resourcegroups/rgname",
        deny_assignment_id="denyAssignmentId",
    )
    print(response)


# x-ms-original-file: specification/authorization/resource-manager/Microsoft.Authorization/stable/2022-04-01/examples/GetDenyAssignmentByNameId.json
if __name__ == "__main__":
    main()
