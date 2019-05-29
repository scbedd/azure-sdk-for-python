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


class OperationDefinition(Model):
    """The definition of a container registry operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The display information for the container registry
     operation.
    :type display:
     ~azure.mgmt.containerregistry.v2017_03_01.models.OperationDisplayDefinition
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayDefinition'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(OperationDefinition, self).__init__(**kwargs)
        self.name = name
        self.display = display
