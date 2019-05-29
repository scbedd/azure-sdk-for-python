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

from .resource_py3 import Resource


class Webhook(Resource):
    """An object that represents a webhook for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be
     changed after the resource is created.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param status: The status of the webhook at the time the operation was
     called. Possible values include: 'enabled', 'disabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.WebhookStatus
    :param scope: The scope of repositories where the event can be triggered.
     For example, 'foo:*' means events for all tags under repository 'foo'.
     'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to
     'foo:latest'. Empty means all events.
    :type scope: str
    :param actions: Required. The list of actions that trigger the webhook to
     post notifications.
    :type actions: list[str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.WebhookAction]
    :ivar provisioning_state: The provisioning state of the webhook at the
     time the operation was called. Possible values include: 'Creating',
     'Updating', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'actions': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'actions': {'key': 'properties.actions', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, actions, tags=None, status=None, scope: str=None, **kwargs) -> None:
        super(Webhook, self).__init__(location=location, tags=tags, **kwargs)
        self.status = status
        self.scope = scope
        self.actions = actions
        self.provisioning_state = None
