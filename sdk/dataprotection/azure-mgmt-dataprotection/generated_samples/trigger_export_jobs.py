# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.dataprotection import DataProtectionMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dataprotection
# USAGE
    python trigger_export_jobs.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataProtectionMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.export_jobs.begin_trigger(
        resource_group_name="SwaggerTestRg",
        vault_name="NetSDKTestRsVault",
    ).result()
    print(response)


# x-ms-original-file: specification/dataprotection/resource-manager/Microsoft.DataProtection/stable/2023-01-01/examples/JobCRUD/TriggerExportJobs.json
if __name__ == "__main__":
    main()
