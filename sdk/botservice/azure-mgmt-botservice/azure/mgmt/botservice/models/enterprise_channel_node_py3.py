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

from msrest.serialization import Model


class EnterpriseChannelNode(Model):
    """The properties specific to an Enterprise Channel Node.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Id of Enterprise Channel Node. This is generated by the Bot
     Framework.
    :vartype id: str
    :param state: The current state of the Enterprise Channel Node. Possible
     values include: 'Creating', 'CreateFailed', 'Started', 'Starting',
     'StartFailed', 'Stopped', 'Stopping', 'StopFailed', 'Deleting',
     'DeleteFailed'
    :type state: str or
     ~azure.mgmt.botservice.models.EnterpriseChannelNodeState
    :param name: Required. The name of the Enterprise Channel Node.
    :type name: str
    :param azure_sku: Required. The sku of the Enterprise Channel Node.
    :type azure_sku: str
    :param azure_location: Required. The location of the Enterprise Channel
     Node.
    :type azure_location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'azure_sku': {'required': True},
        'azure_location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'azure_sku': {'key': 'azureSku', 'type': 'str'},
        'azure_location': {'key': 'azureLocation', 'type': 'str'},
    }

    def __init__(self, *, name: str, azure_sku: str, azure_location: str, state=None, **kwargs) -> None:
        super(EnterpriseChannelNode, self).__init__(**kwargs)
        self.id = None
        self.state = state
        self.name = name
        self.azure_sku = azure_sku
        self.azure_location = azure_location
