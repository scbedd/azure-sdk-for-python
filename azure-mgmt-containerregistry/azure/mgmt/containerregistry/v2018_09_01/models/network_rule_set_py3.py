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


class NetworkRuleSet(Model):
    """The network rule set for a container registry.

    :param default_action: The default action of allow or deny when no other
     rules match. Possible values include: 'Allow', 'Deny'. Default value:
     "Allow" .
    :type default_action: str or
     ~azure.mgmt.containerregistry.v2018_09_01.models.DefaultAction
    :param virtual_network_rules: The virtual network rules
    :type virtual_network_rules:
     list[~azure.mgmt.containerregistry.v2018_09_01.models.VirtualNetworkRule]
    """

    _attribute_map = {
        'default_action': {'key': 'defaultAction', 'type': 'str'},
        'virtual_network_rules': {'key': 'virtualNetworkRules', 'type': '[VirtualNetworkRule]'},
    }

    def __init__(self, *, default_action="Allow", virtual_network_rules=None, **kwargs) -> None:
        super(NetworkRuleSet, self).__init__(**kwargs)
        self.default_action = default_action
        self.virtual_network_rules = virtual_network_rules
