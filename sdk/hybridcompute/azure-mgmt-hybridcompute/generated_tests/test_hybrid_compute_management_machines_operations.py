# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hybridcompute import HybridComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHybridComputeManagementMachinesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HybridComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_delete(self, resource_group):
        response = self.client.machines.delete(
            resource_group_name=resource_group.name,
            machine_name="str",
            api_version="2024-07-10",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.machines.get(
            resource_group_name=resource_group.name,
            machine_name="str",
            api_version="2024-07-10",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_assess_patches(self, resource_group):
        response = self.client.machines.begin_assess_patches(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-07-10",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_install_patches(self, resource_group):
        response = self.client.machines.begin_install_patches(
            resource_group_name=resource_group.name,
            name="str",
            install_patches_input={
                "maximumDuration": "1 day, 0:00:00",
                "rebootSetting": "str",
                "linuxParameters": {
                    "classificationsToInclude": ["str"],
                    "packageNameMasksToExclude": ["str"],
                    "packageNameMasksToInclude": ["str"],
                },
                "windowsParameters": {
                    "classificationsToInclude": ["str"],
                    "excludeKbsRequiringReboot": bool,
                    "kbNumbersToExclude": ["str"],
                    "kbNumbersToInclude": ["str"],
                    "maxPatchPublishDate": "2020-02-20 00:00:00",
                },
            },
            api_version="2024-07-10",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.machines.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-07-10",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.machines.list_by_subscription(
            api_version="2024-07-10",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
