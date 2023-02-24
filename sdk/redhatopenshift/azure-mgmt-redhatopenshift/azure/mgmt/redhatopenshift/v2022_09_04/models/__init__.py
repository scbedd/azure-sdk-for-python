# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import APIServerProfile
from ._models_py3 import CloudErrorBody
from ._models_py3 import ClusterProfile
from ._models_py3 import ConsoleProfile
from ._models_py3 import Display
from ._models_py3 import IngressProfile
from ._models_py3 import MachinePool
from ._models_py3 import MachinePoolList
from ._models_py3 import MachinePoolUpdate
from ._models_py3 import MasterProfile
from ._models_py3 import NetworkProfile
from ._models_py3 import OpenShiftCluster
from ._models_py3 import OpenShiftClusterAdminKubeconfig
from ._models_py3 import OpenShiftClusterCredentials
from ._models_py3 import OpenShiftClusterList
from ._models_py3 import OpenShiftClusterUpdate
from ._models_py3 import OpenShiftVersion
from ._models_py3 import OpenShiftVersionList
from ._models_py3 import Operation
from ._models_py3 import OperationList
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import Secret
from ._models_py3 import SecretList
from ._models_py3 import SecretUpdate
from ._models_py3 import ServicePrincipalProfile
from ._models_py3 import SyncIdentityProvider
from ._models_py3 import SyncIdentityProviderList
from ._models_py3 import SyncIdentityProviderUpdate
from ._models_py3 import SyncSet
from ._models_py3 import SyncSetList
from ._models_py3 import SyncSetUpdate
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import WorkerProfile

from ._azure_red_hat_open_shift_client_enums import CreatedByType
from ._azure_red_hat_open_shift_client_enums import EncryptionAtHost
from ._azure_red_hat_open_shift_client_enums import FipsValidatedModules
from ._azure_red_hat_open_shift_client_enums import ProvisioningState
from ._azure_red_hat_open_shift_client_enums import Visibility
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "APIServerProfile",
    "CloudErrorBody",
    "ClusterProfile",
    "ConsoleProfile",
    "Display",
    "IngressProfile",
    "MachinePool",
    "MachinePoolList",
    "MachinePoolUpdate",
    "MasterProfile",
    "NetworkProfile",
    "OpenShiftCluster",
    "OpenShiftClusterAdminKubeconfig",
    "OpenShiftClusterCredentials",
    "OpenShiftClusterList",
    "OpenShiftClusterUpdate",
    "OpenShiftVersion",
    "OpenShiftVersionList",
    "Operation",
    "OperationList",
    "ProxyResource",
    "Resource",
    "Secret",
    "SecretList",
    "SecretUpdate",
    "ServicePrincipalProfile",
    "SyncIdentityProvider",
    "SyncIdentityProviderList",
    "SyncIdentityProviderUpdate",
    "SyncSet",
    "SyncSetList",
    "SyncSetUpdate",
    "SystemData",
    "TrackedResource",
    "WorkerProfile",
    "CreatedByType",
    "EncryptionAtHost",
    "FipsValidatedModules",
    "ProvisioningState",
    "Visibility",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
