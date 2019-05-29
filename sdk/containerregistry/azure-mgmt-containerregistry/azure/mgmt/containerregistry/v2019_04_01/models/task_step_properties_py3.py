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


class TaskStepProperties(Model):
    """Base properties for any task step.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DockerBuildStep, FileTaskStep, EncodedTaskStep

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar base_image_dependencies: List of base image dependencies for a step.
    :vartype base_image_dependencies:
     list[~azure.mgmt.containerregistry.v2019_04_01.models.BaseImageDependency]
    :param context_path: The URL(absolute or relative) of the source context
     for the task step.
    :type context_path: str
    :param context_access_token: The token (git PAT or SAS token of storage
     account blob) associated with the context for a step.
    :type context_access_token: str
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'base_image_dependencies': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'base_image_dependencies': {'key': 'baseImageDependencies', 'type': '[BaseImageDependency]'},
        'context_path': {'key': 'contextPath', 'type': 'str'},
        'context_access_token': {'key': 'contextAccessToken', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Docker': 'DockerBuildStep', 'FileTask': 'FileTaskStep', 'EncodedTask': 'EncodedTaskStep'}
    }

    def __init__(self, *, context_path: str=None, context_access_token: str=None, **kwargs) -> None:
        super(TaskStepProperties, self).__init__(**kwargs)
        self.base_image_dependencies = None
        self.context_path = context_path
        self.context_access_token = context_access_token
        self.type = None
