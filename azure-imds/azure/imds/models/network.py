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


class Network(Model):
    """Network Metadata.

    :param interface:
    :type interface: list[~azure.imds.models.NetworkInterface]
    """

    _attribute_map = {
        'interface': {'key': 'interface', 'type': '[NetworkInterface]'},
    }

    def __init__(self, **kwargs):
        super(Network, self).__init__(**kwargs)
        self.interface = kwargs.get('interface', None)
