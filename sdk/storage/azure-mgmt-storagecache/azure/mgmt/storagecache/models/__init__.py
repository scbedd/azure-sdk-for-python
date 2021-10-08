# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApiOperation
    from ._models_py3 import ApiOperationDisplay
    from ._models_py3 import ApiOperationListResult
    from ._models_py3 import ApiOperationPropertiesServiceSpecification
    from ._models_py3 import AscOperation
    from ._models_py3 import BlobNfsTarget
    from ._models_py3 import Cache
    from ._models_py3 import CacheActiveDirectorySettings
    from ._models_py3 import CacheActiveDirectorySettingsCredentials
    from ._models_py3 import CacheDirectorySettings
    from ._models_py3 import CacheEncryptionSettings
    from ._models_py3 import CacheHealth
    from ._models_py3 import CacheIdentity
    from ._models_py3 import CacheNetworkSettings
    from ._models_py3 import CacheSecuritySettings
    from ._models_py3 import CacheSku
    from ._models_py3 import CacheUpgradeStatus
    from ._models_py3 import CacheUsernameDownloadSettings
    from ._models_py3 import CacheUsernameDownloadSettingsCredentials
    from ._models_py3 import CachesListResult
    from ._models_py3 import ClfsTarget
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import Condition
    from ._models_py3 import ErrorResponse
    from ._models_py3 import KeyVaultKeyReference
    from ._models_py3 import KeyVaultKeyReferenceSourceVault
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NamespaceJunction
    from ._models_py3 import Nfs3Target
    from ._models_py3 import NfsAccessPolicy
    from ._models_py3 import NfsAccessRule
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuCapabilities
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkusResult
    from ._models_py3 import Restriction
    from ._models_py3 import StorageTarget
    from ._models_py3 import StorageTargetResource
    from ._models_py3 import StorageTargetsResult
    from ._models_py3 import SystemData
    from ._models_py3 import UnknownTarget
    from ._models_py3 import UsageModel
    from ._models_py3 import UsageModelDisplay
    from ._models_py3 import UsageModelsResult
    from ._models_py3 import UserAssignedIdentitiesValue
except (SyntaxError, ImportError):
    from ._models import ApiOperation  # type: ignore
    from ._models import ApiOperationDisplay  # type: ignore
    from ._models import ApiOperationListResult  # type: ignore
    from ._models import ApiOperationPropertiesServiceSpecification  # type: ignore
    from ._models import AscOperation  # type: ignore
    from ._models import BlobNfsTarget  # type: ignore
    from ._models import Cache  # type: ignore
    from ._models import CacheActiveDirectorySettings  # type: ignore
    from ._models import CacheActiveDirectorySettingsCredentials  # type: ignore
    from ._models import CacheDirectorySettings  # type: ignore
    from ._models import CacheEncryptionSettings  # type: ignore
    from ._models import CacheHealth  # type: ignore
    from ._models import CacheIdentity  # type: ignore
    from ._models import CacheNetworkSettings  # type: ignore
    from ._models import CacheSecuritySettings  # type: ignore
    from ._models import CacheSku  # type: ignore
    from ._models import CacheUpgradeStatus  # type: ignore
    from ._models import CacheUsernameDownloadSettings  # type: ignore
    from ._models import CacheUsernameDownloadSettingsCredentials  # type: ignore
    from ._models import CachesListResult  # type: ignore
    from ._models import ClfsTarget  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import Condition  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import KeyVaultKeyReference  # type: ignore
    from ._models import KeyVaultKeyReferenceSourceVault  # type: ignore
    from ._models import MetricDimension  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import NamespaceJunction  # type: ignore
    from ._models import Nfs3Target  # type: ignore
    from ._models import NfsAccessPolicy  # type: ignore
    from ._models import NfsAccessRule  # type: ignore
    from ._models import ResourceSku  # type: ignore
    from ._models import ResourceSkuCapabilities  # type: ignore
    from ._models import ResourceSkuLocationInfo  # type: ignore
    from ._models import ResourceSkusResult  # type: ignore
    from ._models import Restriction  # type: ignore
    from ._models import StorageTarget  # type: ignore
    from ._models import StorageTargetResource  # type: ignore
    from ._models import StorageTargetsResult  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import UnknownTarget  # type: ignore
    from ._models import UsageModel  # type: ignore
    from ._models import UsageModelDisplay  # type: ignore
    from ._models import UsageModelsResult  # type: ignore
    from ._models import UserAssignedIdentitiesValue  # type: ignore

from ._storage_cache_management_client_enums import (
    CacheIdentityType,
    CreatedByType,
    DomainJoinedType,
    FirmwareStatusType,
    HealthStateType,
    MetricAggregationType,
    NfsAccessRuleAccess,
    NfsAccessRuleScope,
    OperationalStateType,
    ProvisioningStateType,
    ReasonCode,
    StorageTargetType,
    UsernameDownloadedType,
    UsernameSource,
)

__all__ = [
    'ApiOperation',
    'ApiOperationDisplay',
    'ApiOperationListResult',
    'ApiOperationPropertiesServiceSpecification',
    'AscOperation',
    'BlobNfsTarget',
    'Cache',
    'CacheActiveDirectorySettings',
    'CacheActiveDirectorySettingsCredentials',
    'CacheDirectorySettings',
    'CacheEncryptionSettings',
    'CacheHealth',
    'CacheIdentity',
    'CacheNetworkSettings',
    'CacheSecuritySettings',
    'CacheSku',
    'CacheUpgradeStatus',
    'CacheUsernameDownloadSettings',
    'CacheUsernameDownloadSettingsCredentials',
    'CachesListResult',
    'ClfsTarget',
    'CloudErrorBody',
    'Condition',
    'ErrorResponse',
    'KeyVaultKeyReference',
    'KeyVaultKeyReferenceSourceVault',
    'MetricDimension',
    'MetricSpecification',
    'NamespaceJunction',
    'Nfs3Target',
    'NfsAccessPolicy',
    'NfsAccessRule',
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuLocationInfo',
    'ResourceSkusResult',
    'Restriction',
    'StorageTarget',
    'StorageTargetResource',
    'StorageTargetsResult',
    'SystemData',
    'UnknownTarget',
    'UsageModel',
    'UsageModelDisplay',
    'UsageModelsResult',
    'UserAssignedIdentitiesValue',
    'CacheIdentityType',
    'CreatedByType',
    'DomainJoinedType',
    'FirmwareStatusType',
    'HealthStateType',
    'MetricAggregationType',
    'NfsAccessRuleAccess',
    'NfsAccessRuleScope',
    'OperationalStateType',
    'ProvisioningStateType',
    'ReasonCode',
    'StorageTargetType',
    'UsernameDownloadedType',
    'UsernameSource',
]
