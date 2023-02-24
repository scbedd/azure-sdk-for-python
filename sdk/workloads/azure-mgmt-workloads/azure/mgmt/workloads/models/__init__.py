# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApplicationServerConfiguration
from ._models_py3 import ApplicationServerFullResourceNames
from ._models_py3 import ApplicationServerVmDetails
from ._models_py3 import CentralServerConfiguration
from ._models_py3 import CentralServerFullResourceNames
from ._models_py3 import CentralServerVmDetails
from ._models_py3 import CreateAndMountFileShareConfiguration
from ._models_py3 import DB2ProviderInstanceProperties
from ._models_py3 import DatabaseConfiguration
from ._models_py3 import DatabaseServerFullResourceNames
from ._models_py3 import DatabaseVmDetails
from ._models_py3 import DeployerVmPackages
from ._models_py3 import DeploymentConfiguration
from ._models_py3 import DeploymentWithOSConfiguration
from ._models_py3 import DiscoveryConfiguration
from ._models_py3 import DiskConfiguration
from ._models_py3 import DiskDetails
from ._models_py3 import DiskSku
from ._models_py3 import DiskVolumeConfiguration
from ._models_py3 import EnqueueReplicationServerProperties
from ._models_py3 import EnqueueServerProperties
from ._models_py3 import Error
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDefinition
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorInnerError
from ._models_py3 import ErrorResponse
from ._models_py3 import ExternalInstallationSoftwareConfiguration
from ._models_py3 import FileShareConfiguration
from ._models_py3 import GatewayServerProperties
from ._models_py3 import HanaDbProviderInstanceProperties
from ._models_py3 import HighAvailabilityConfiguration
from ._models_py3 import HighAvailabilitySoftwareConfiguration
from ._models_py3 import ImageReference
from ._models_py3 import InfrastructureConfiguration
from ._models_py3 import LinuxConfiguration
from ._models_py3 import LoadBalancerDetails
from ._models_py3 import LoadBalancerResourceNames
from ._models_py3 import ManagedRGConfiguration
from ._models_py3 import MessageServerProperties
from ._models_py3 import Monitor
from ._models_py3 import MonitorListResult
from ._models_py3 import MonitorPropertiesErrors
from ._models_py3 import MountFileShareConfiguration
from ._models_py3 import MsSqlServerProviderInstanceProperties
from ._models_py3 import NetworkConfiguration
from ._models_py3 import NetworkInterfaceResourceNames
from ._models_py3 import OSConfiguration
from ._models_py3 import OSProfile
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationStatusResult
from ._models_py3 import OperationsContent
from ._models_py3 import OperationsDefinition
from ._models_py3 import OperationsDefinitionArrayResponseWithContinuation
from ._models_py3 import OperationsDefinitionDisplay
from ._models_py3 import OperationsDisplayDefinition
from ._models_py3 import OsSapConfiguration
from ._models_py3 import PrometheusHaClusterProviderInstanceProperties
from ._models_py3 import PrometheusOSProviderInstanceProperties
from ._models_py3 import ProviderInstance
from ._models_py3 import ProviderInstanceListResult
from ._models_py3 import ProviderInstancePropertiesErrors
from ._models_py3 import ProviderSpecificProperties
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import SAPApplicationServerInstance
from ._models_py3 import SAPApplicationServerInstanceList
from ._models_py3 import SAPAvailabilityZoneDetailsRequest
from ._models_py3 import SAPAvailabilityZoneDetailsResult
from ._models_py3 import SAPAvailabilityZonePair
from ._models_py3 import SAPCentralInstanceList
from ._models_py3 import SAPCentralServerInstance
from ._models_py3 import SAPConfiguration
from ._models_py3 import SAPDatabaseInstance
from ._models_py3 import SAPDatabaseInstanceList
from ._models_py3 import SAPDiskConfiguration
from ._models_py3 import SAPDiskConfigurationsRequest
from ._models_py3 import SAPDiskConfigurationsResult
from ._models_py3 import SAPInstallWithoutOSConfigSoftwareConfiguration
from ._models_py3 import SAPSizingRecommendationRequest
from ._models_py3 import SAPSizingRecommendationResult
from ._models_py3 import SAPSupportedResourceSkusResult
from ._models_py3 import SAPSupportedSku
from ._models_py3 import SAPSupportedSkusRequest
from ._models_py3 import SAPVirtualInstance
from ._models_py3 import SAPVirtualInstanceError
from ._models_py3 import SAPVirtualInstanceList
from ._models_py3 import SapLandscapeMonitor
from ._models_py3 import SapLandscapeMonitorListResult
from ._models_py3 import SapLandscapeMonitorMetricThresholds
from ._models_py3 import SapLandscapeMonitorPropertiesGrouping
from ._models_py3 import SapLandscapeMonitorSidMapping
from ._models_py3 import SapNetWeaverProviderInstanceProperties
from ._models_py3 import ServiceInitiatedSoftwareConfiguration
from ._models_py3 import SharedStorageResourceNames
from ._models_py3 import SingleServerConfiguration
from ._models_py3 import SingleServerCustomResourceNames
from ._models_py3 import SingleServerFullResourceNames
from ._models_py3 import SingleServerRecommendationResult
from ._models_py3 import SkipFileShareConfiguration
from ._models_py3 import SoftwareConfiguration
from ._models_py3 import SshConfiguration
from ._models_py3 import SshKeyPair
from ._models_py3 import SshPublicKey
from ._models_py3 import StopRequest
from ._models_py3 import StorageConfiguration
from ._models_py3 import StorageInformation
from ._models_py3 import SystemData
from ._models_py3 import Tags
from ._models_py3 import ThreeTierConfiguration
from ._models_py3 import ThreeTierCustomResourceNames
from ._models_py3 import ThreeTierFullResourceNames
from ._models_py3 import ThreeTierRecommendationResult
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateMonitorRequest
from ._models_py3 import UpdateSAPApplicationInstanceRequest
from ._models_py3 import UpdateSAPCentralInstanceRequest
from ._models_py3 import UpdateSAPDatabaseInstanceRequest
from ._models_py3 import UpdateSAPVirtualInstanceRequest
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import UserAssignedServiceIdentity
from ._models_py3 import VirtualMachineConfiguration
from ._models_py3 import VirtualMachineResourceNames
from ._models_py3 import WindowsConfiguration

from ._workloads_client_enums import ActionType
from ._workloads_client_enums import ApplicationServerVirtualMachineType
from ._workloads_client_enums import CentralServerVirtualMachineType
from ._workloads_client_enums import ConfigurationType
from ._workloads_client_enums import CreatedByType
from ._workloads_client_enums import DiskSkuName
from ._workloads_client_enums import EnqueueReplicationServerType
from ._workloads_client_enums import ManagedServiceIdentityType
from ._workloads_client_enums import NamingPatternType
from ._workloads_client_enums import OSType
from ._workloads_client_enums import OperationProperties
from ._workloads_client_enums import Origin
from ._workloads_client_enums import RoutingPreference
from ._workloads_client_enums import SAPConfigurationType
from ._workloads_client_enums import SAPDatabaseScaleMethod
from ._workloads_client_enums import SAPDatabaseType
from ._workloads_client_enums import SAPDeploymentType
from ._workloads_client_enums import SAPEnvironmentType
from ._workloads_client_enums import SAPHealthState
from ._workloads_client_enums import SAPHighAvailabilityType
from ._workloads_client_enums import SAPProductType
from ._workloads_client_enums import SAPSoftwareInstallationType
from ._workloads_client_enums import SAPVirtualInstanceState
from ._workloads_client_enums import SAPVirtualInstanceStatus
from ._workloads_client_enums import SapLandscapeMonitorProvisioningState
from ._workloads_client_enums import SapVirtualInstanceProvisioningState
from ._workloads_client_enums import SslPreference
from ._workloads_client_enums import WorkloadMonitorActionType
from ._workloads_client_enums import WorkloadMonitorProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApplicationServerConfiguration",
    "ApplicationServerFullResourceNames",
    "ApplicationServerVmDetails",
    "CentralServerConfiguration",
    "CentralServerFullResourceNames",
    "CentralServerVmDetails",
    "CreateAndMountFileShareConfiguration",
    "DB2ProviderInstanceProperties",
    "DatabaseConfiguration",
    "DatabaseServerFullResourceNames",
    "DatabaseVmDetails",
    "DeployerVmPackages",
    "DeploymentConfiguration",
    "DeploymentWithOSConfiguration",
    "DiscoveryConfiguration",
    "DiskConfiguration",
    "DiskDetails",
    "DiskSku",
    "DiskVolumeConfiguration",
    "EnqueueReplicationServerProperties",
    "EnqueueServerProperties",
    "Error",
    "ErrorAdditionalInfo",
    "ErrorDefinition",
    "ErrorDetail",
    "ErrorInnerError",
    "ErrorResponse",
    "ExternalInstallationSoftwareConfiguration",
    "FileShareConfiguration",
    "GatewayServerProperties",
    "HanaDbProviderInstanceProperties",
    "HighAvailabilityConfiguration",
    "HighAvailabilitySoftwareConfiguration",
    "ImageReference",
    "InfrastructureConfiguration",
    "LinuxConfiguration",
    "LoadBalancerDetails",
    "LoadBalancerResourceNames",
    "ManagedRGConfiguration",
    "MessageServerProperties",
    "Monitor",
    "MonitorListResult",
    "MonitorPropertiesErrors",
    "MountFileShareConfiguration",
    "MsSqlServerProviderInstanceProperties",
    "NetworkConfiguration",
    "NetworkInterfaceResourceNames",
    "OSConfiguration",
    "OSProfile",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationStatusResult",
    "OperationsContent",
    "OperationsDefinition",
    "OperationsDefinitionArrayResponseWithContinuation",
    "OperationsDefinitionDisplay",
    "OperationsDisplayDefinition",
    "OsSapConfiguration",
    "PrometheusHaClusterProviderInstanceProperties",
    "PrometheusOSProviderInstanceProperties",
    "ProviderInstance",
    "ProviderInstanceListResult",
    "ProviderInstancePropertiesErrors",
    "ProviderSpecificProperties",
    "ProxyResource",
    "Resource",
    "SAPApplicationServerInstance",
    "SAPApplicationServerInstanceList",
    "SAPAvailabilityZoneDetailsRequest",
    "SAPAvailabilityZoneDetailsResult",
    "SAPAvailabilityZonePair",
    "SAPCentralInstanceList",
    "SAPCentralServerInstance",
    "SAPConfiguration",
    "SAPDatabaseInstance",
    "SAPDatabaseInstanceList",
    "SAPDiskConfiguration",
    "SAPDiskConfigurationsRequest",
    "SAPDiskConfigurationsResult",
    "SAPInstallWithoutOSConfigSoftwareConfiguration",
    "SAPSizingRecommendationRequest",
    "SAPSizingRecommendationResult",
    "SAPSupportedResourceSkusResult",
    "SAPSupportedSku",
    "SAPSupportedSkusRequest",
    "SAPVirtualInstance",
    "SAPVirtualInstanceError",
    "SAPVirtualInstanceList",
    "SapLandscapeMonitor",
    "SapLandscapeMonitorListResult",
    "SapLandscapeMonitorMetricThresholds",
    "SapLandscapeMonitorPropertiesGrouping",
    "SapLandscapeMonitorSidMapping",
    "SapNetWeaverProviderInstanceProperties",
    "ServiceInitiatedSoftwareConfiguration",
    "SharedStorageResourceNames",
    "SingleServerConfiguration",
    "SingleServerCustomResourceNames",
    "SingleServerFullResourceNames",
    "SingleServerRecommendationResult",
    "SkipFileShareConfiguration",
    "SoftwareConfiguration",
    "SshConfiguration",
    "SshKeyPair",
    "SshPublicKey",
    "StopRequest",
    "StorageConfiguration",
    "StorageInformation",
    "SystemData",
    "Tags",
    "ThreeTierConfiguration",
    "ThreeTierCustomResourceNames",
    "ThreeTierFullResourceNames",
    "ThreeTierRecommendationResult",
    "TrackedResource",
    "UpdateMonitorRequest",
    "UpdateSAPApplicationInstanceRequest",
    "UpdateSAPCentralInstanceRequest",
    "UpdateSAPDatabaseInstanceRequest",
    "UpdateSAPVirtualInstanceRequest",
    "UserAssignedIdentity",
    "UserAssignedServiceIdentity",
    "VirtualMachineConfiguration",
    "VirtualMachineResourceNames",
    "WindowsConfiguration",
    "ActionType",
    "ApplicationServerVirtualMachineType",
    "CentralServerVirtualMachineType",
    "ConfigurationType",
    "CreatedByType",
    "DiskSkuName",
    "EnqueueReplicationServerType",
    "ManagedServiceIdentityType",
    "NamingPatternType",
    "OSType",
    "OperationProperties",
    "Origin",
    "RoutingPreference",
    "SAPConfigurationType",
    "SAPDatabaseScaleMethod",
    "SAPDatabaseType",
    "SAPDeploymentType",
    "SAPEnvironmentType",
    "SAPHealthState",
    "SAPHighAvailabilityType",
    "SAPProductType",
    "SAPSoftwareInstallationType",
    "SAPVirtualInstanceState",
    "SAPVirtualInstanceStatus",
    "SapLandscapeMonitorProvisioningState",
    "SapVirtualInstanceProvisioningState",
    "SslPreference",
    "WorkloadMonitorActionType",
    "WorkloadMonitorProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
