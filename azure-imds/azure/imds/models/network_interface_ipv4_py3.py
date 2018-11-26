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


class NetworkInterfaceIpv4(Model):
    """NetworkInterfaceIpv4.

    :param ip_address:
    :type ip_address: list[~azure.imds.models.Ipv4Properties]
    :param subnet:
    :type subnet: list[~azure.imds.models.SubnetProperties]
    """

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': '[Ipv4Properties]'},
        'subnet': {'key': 'subnet', 'type': '[SubnetProperties]'},
    }

    def __init__(self, *, ip_address=None, subnet=None, **kwargs) -> None:
        super(NetworkInterfaceIpv4, self).__init__(**kwargs)
        self.ip_address = ip_address
        self.subnet = subnet
