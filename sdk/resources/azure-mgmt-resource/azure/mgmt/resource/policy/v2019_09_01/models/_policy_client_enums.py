# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class EnforcementMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The policy assignment enforcement mode. Possible values are Default and DoNotEnforce."""

    DEFAULT = "Default"
    """The policy effect is enforced during resource creation or update."""
    DO_NOT_ENFORCE = "DoNotEnforce"
    """The policy effect is not enforced during resource creation or update."""


class ParameterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The data type of the parameter."""

    STRING = "String"
    ARRAY = "Array"
    OBJECT = "Object"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
    FLOAT = "Float"
    DATE_TIME = "DateTime"


class PolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static."""

    NOT_SPECIFIED = "NotSpecified"
    BUILT_IN = "BuiltIn"
    CUSTOM = "Custom"
    STATIC = "Static"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type. This is the only required field when adding a system assigned identity to a
    resource.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    """Indicates that a system assigned identity is associated with the resource."""
    NONE = "None"
    """Indicates that no identity is associated with the resource or that the existing identity should
    #: be removed."""
