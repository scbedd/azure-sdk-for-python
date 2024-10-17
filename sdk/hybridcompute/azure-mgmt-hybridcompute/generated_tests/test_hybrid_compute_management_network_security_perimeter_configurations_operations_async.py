# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hybridcompute.aio import HybridComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHybridComputeManagementNetworkSecurityPerimeterConfigurationsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HybridComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_by_private_link_scope(self, resource_group):
        response = await self.client.network_security_perimeter_configurations.get_by_private_link_scope(
            resource_group_name=resource_group.name,
            scope_name="str",
            perimeter_name="str",
            api_version="2024-07-10",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_private_link_scope(self, resource_group):
        response = self.client.network_security_perimeter_configurations.list_by_private_link_scope(
            resource_group_name=resource_group.name,
            scope_name="str",
            api_version="2024-07-10",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_reconcile_for_private_link_scope(self, resource_group):
        response = await (
            await self.client.network_security_perimeter_configurations.begin_reconcile_for_private_link_scope(
                resource_group_name=resource_group.name,
                scope_name="str",
                perimeter_name="str",
                api_version="2024-07-10",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
