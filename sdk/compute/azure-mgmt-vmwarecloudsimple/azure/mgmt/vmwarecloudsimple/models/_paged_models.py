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

from msrest.paging import Paged


class AvailableOperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AvailableOperation <azure.mgmt.vmwarecloudsimple.models.AvailableOperation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AvailableOperation]'}
    }

    def __init__(self, *args, **kwargs):

        super(AvailableOperationPaged, self).__init__(*args, **kwargs)
class DedicatedCloudNodePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DedicatedCloudNode <azure.mgmt.vmwarecloudsimple.models.DedicatedCloudNode>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DedicatedCloudNode]'}
    }

    def __init__(self, *args, **kwargs):

        super(DedicatedCloudNodePaged, self).__init__(*args, **kwargs)
class DedicatedCloudServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DedicatedCloudService <azure.mgmt.vmwarecloudsimple.models.DedicatedCloudService>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DedicatedCloudService]'}
    }

    def __init__(self, *args, **kwargs):

        super(DedicatedCloudServicePaged, self).__init__(*args, **kwargs)
class SkuAvailabilityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SkuAvailability <azure.mgmt.vmwarecloudsimple.models.SkuAvailability>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SkuAvailability]'}
    }

    def __init__(self, *args, **kwargs):

        super(SkuAvailabilityPaged, self).__init__(*args, **kwargs)
class PrivateCloudPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateCloud <azure.mgmt.vmwarecloudsimple.models.PrivateCloud>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateCloud]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateCloudPaged, self).__init__(*args, **kwargs)
class CustomizationPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CustomizationPolicy <azure.mgmt.vmwarecloudsimple.models.CustomizationPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CustomizationPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(CustomizationPolicyPaged, self).__init__(*args, **kwargs)
class ResourcePoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourcePool <azure.mgmt.vmwarecloudsimple.models.ResourcePool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourcePool]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourcePoolPaged, self).__init__(*args, **kwargs)
class VirtualMachineTemplatePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachineTemplate <azure.mgmt.vmwarecloudsimple.models.VirtualMachineTemplate>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachineTemplate]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachineTemplatePaged, self).__init__(*args, **kwargs)
class VirtualNetworkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetwork <azure.mgmt.vmwarecloudsimple.models.VirtualNetwork>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetwork]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.vmwarecloudsimple.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class VirtualMachinePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachine <azure.mgmt.vmwarecloudsimple.models.VirtualMachine>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachine]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachinePaged, self).__init__(*args, **kwargs)
