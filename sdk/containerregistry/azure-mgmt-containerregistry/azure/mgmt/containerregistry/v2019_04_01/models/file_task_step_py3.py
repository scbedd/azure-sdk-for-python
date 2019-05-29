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

from .task_step_properties_py3 import TaskStepProperties


class FileTaskStep(TaskStepProperties):
    """The properties of a task step.

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
    :param task_file_path: Required. The task template/definition file path
     relative to the source context.
    :type task_file_path: str
    :param values_file_path: The task values/parameters file path relative to
     the source context.
    :type values_file_path: str
    :param values: The collection of overridable values that can be passed
     when running a task.
    :type values:
     list[~azure.mgmt.containerregistry.v2019_04_01.models.SetValue]
    """

    _validation = {
        'base_image_dependencies': {'readonly': True},
        'type': {'required': True},
        'task_file_path': {'required': True},
    }

    _attribute_map = {
        'base_image_dependencies': {'key': 'baseImageDependencies', 'type': '[BaseImageDependency]'},
        'context_path': {'key': 'contextPath', 'type': 'str'},
        'context_access_token': {'key': 'contextAccessToken', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'task_file_path': {'key': 'taskFilePath', 'type': 'str'},
        'values_file_path': {'key': 'valuesFilePath', 'type': 'str'},
        'values': {'key': 'values', 'type': '[SetValue]'},
    }

    def __init__(self, *, task_file_path: str, context_path: str=None, context_access_token: str=None, values_file_path: str=None, values=None, **kwargs) -> None:
        super(FileTaskStep, self).__init__(context_path=context_path, context_access_token=context_access_token, **kwargs)
        self.task_file_path = task_file_path
        self.values_file_path = values_file_path
        self.values = values
        self.type = 'FileTask'
