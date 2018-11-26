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


class Ipv6Properties(Model):
    """Ipv6Properties.

    :param private_ip_address: This is the private IPV6 address assigned to
     the interface.
    :type private_ip_address: str
    """

    _attribute_map = {
        'private_ip_address': {'key': 'privateIpAddress', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Ipv6Properties, self).__init__(**kwargs)
        self.private_ip_address = kwargs.get('private_ip_address', None)
