# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AssociationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Association Type Enum."""

    SUBNETS = "subnets"
    """Association of Type Subnet"""


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class PolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Policy Type of the Security Policy."""

    WAF = "waf"
    """Policy of Type WAF"""


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource Provisioning State Enum."""

    PROVISIONING = "Provisioning"
    """Resource in Provisioning State"""
    UPDATING = "Updating"
    """Resource in Updating State"""
    DELETING = "Deleting"
    """Resource in Deleting State"""
    ACCEPTED = "Accepted"
    """Resource in Accepted State"""
    SUCCEEDED = "Succeeded"
    """Resource in Succeeded State"""
    FAILED = "Failed"
    """Resource in Failed State"""
    CANCELED = "Canceled"
    """Resource in Canceled State"""
