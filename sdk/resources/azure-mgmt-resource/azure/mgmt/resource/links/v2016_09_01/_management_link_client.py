# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import ManagementLinkClientConfiguration
from .operations import Operations
from .operations import ResourceLinksOperations
from . import models


class ManagementLinkClient(SDKClient):
    """Azure resources can be linked together to form logical relationships. You can establish links between resources belonging to different resource groups. However, all the linked resources must belong to the same subscription. Each resource can be linked to 50 other resources. If any of the linked resources are deleted or moved, the link owner must clean up the remaining link.

    :ivar config: Configuration for client.
    :vartype config: ManagementLinkClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resource.links.v2016_09_01.operations.Operations
    :ivar resource_links: ResourceLinks operations
    :vartype resource_links: azure.mgmt.resource.links.v2016_09_01.operations.ResourceLinksOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ManagementLinkClientConfiguration(credentials, subscription_id, base_url)
        super(ManagementLinkClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-09-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_links = ResourceLinksOperations(
            self._client, self.config, self._serialize, self._deserialize)
