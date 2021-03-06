# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccountCredentialDetails
    from ._models_py3 import AddressValidationOutput
    from ._models_py3 import AddressValidationProperties
    from ._models_py3 import ApplianceNetworkConfiguration
    from ._models_py3 import ArmBaseObject
    from ._models_py3 import AvailableSkuRequest
    from ._models_py3 import AvailableSkusResult
    from ._models_py3 import CancellationReason
    from ._models_py3 import CloudError
    from ._models_py3 import ContactDetails
    from ._models_py3 import CopyLogDetails
    from ._models_py3 import CopyProgress
    from ._models_py3 import CreateJobValidations
    from ._models_py3 import CreateOrderLimitForSubscriptionValidationRequest
    from ._models_py3 import CreateOrderLimitForSubscriptionValidationResponseProperties
    from ._models_py3 import DataBoxAccountCopyLogDetails
    from ._models_py3 import DataBoxDiskCopyLogDetails
    from ._models_py3 import DataBoxDiskCopyProgress
    from ._models_py3 import DataBoxDiskJobDetails
    from ._models_py3 import DataBoxDiskJobSecrets
    from ._models_py3 import DataBoxHeavyAccountCopyLogDetails
    from ._models_py3 import DataBoxHeavyJobDetails
    from ._models_py3 import DataBoxHeavyJobSecrets
    from ._models_py3 import DataBoxHeavySecret
    from ._models_py3 import DataBoxJobDetails
    from ._models_py3 import DataBoxScheduleAvailabilityRequest
    from ._models_py3 import DataBoxSecret
    from ._models_py3 import DataDestinationDetailsValidationRequest
    from ._models_py3 import DataDestinationDetailsValidationResponseProperties
    from ._models_py3 import DataboxJobSecrets
    from ._models_py3 import DcAccessSecurityCode
    from ._models_py3 import DestinationAccountDetails
    from ._models_py3 import DestinationManagedDiskDetails
    from ._models_py3 import DestinationStorageAccountDetails
    from ._models_py3 import DestinationToServiceLocationMap
    from ._models_py3 import DiskScheduleAvailabilityRequest
    from ._models_py3 import DiskSecret
    from ._models_py3 import Error
    from ._models_py3 import HeavyScheduleAvailabilityRequest
    from ._models_py3 import JobDeliveryInfo
    from ._models_py3 import JobDetails
    from ._models_py3 import JobErrorDetails
    from ._models_py3 import JobResource
    from ._models_py3 import JobResourceList
    from ._models_py3 import JobResourceUpdateParameter
    from ._models_py3 import JobSecrets
    from ._models_py3 import JobStages
    from ._models_py3 import NotificationPreference
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationList
    from ._models_py3 import PackageShippingDetails
    from ._models_py3 import Preferences
    from ._models_py3 import PreferencesValidationRequest
    from ._models_py3 import PreferencesValidationResponseProperties
    from ._models_py3 import RegionConfigurationRequest
    from ._models_py3 import RegionConfigurationResponse
    from ._models_py3 import Resource
    from ._models_py3 import ScheduleAvailabilityRequest
    from ._models_py3 import ScheduleAvailabilityResponse
    from ._models_py3 import ShareCredentialDetails
    from ._models_py3 import ShipmentPickUpRequest
    from ._models_py3 import ShipmentPickUpResponse
    from ._models_py3 import ShippingAddress
    from ._models_py3 import Sku
    from ._models_py3 import SkuAvailabilityValidationRequest
    from ._models_py3 import SkuAvailabilityValidationResponseProperties
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SkuCost
    from ._models_py3 import SkuInformation
    from ._models_py3 import SubscriptionIsAllowedToCreateJobValidationRequest
    from ._models_py3 import SubscriptionIsAllowedToCreateJobValidationResponseProperties
    from ._models_py3 import TransportAvailabilityDetails
    from ._models_py3 import TransportAvailabilityRequest
    from ._models_py3 import TransportAvailabilityResponse
    from ._models_py3 import TransportPreferences
    from ._models_py3 import UnencryptedCredentials
    from ._models_py3 import UnencryptedCredentialsList
    from ._models_py3 import UpdateJobDetails
    from ._models_py3 import ValidateAddress
    from ._models_py3 import ValidationInputRequest
    from ._models_py3 import ValidationInputResponse
    from ._models_py3 import ValidationRequest
    from ._models_py3 import ValidationResponse
except (SyntaxError, ImportError):
    from ._models import AccountCredentialDetails  # type: ignore
    from ._models import AddressValidationOutput  # type: ignore
    from ._models import AddressValidationProperties  # type: ignore
    from ._models import ApplianceNetworkConfiguration  # type: ignore
    from ._models import ArmBaseObject  # type: ignore
    from ._models import AvailableSkuRequest  # type: ignore
    from ._models import AvailableSkusResult  # type: ignore
    from ._models import CancellationReason  # type: ignore
    from ._models import CloudError  # type: ignore
    from ._models import ContactDetails  # type: ignore
    from ._models import CopyLogDetails  # type: ignore
    from ._models import CopyProgress  # type: ignore
    from ._models import CreateJobValidations  # type: ignore
    from ._models import CreateOrderLimitForSubscriptionValidationRequest  # type: ignore
    from ._models import CreateOrderLimitForSubscriptionValidationResponseProperties  # type: ignore
    from ._models import DataBoxAccountCopyLogDetails  # type: ignore
    from ._models import DataBoxDiskCopyLogDetails  # type: ignore
    from ._models import DataBoxDiskCopyProgress  # type: ignore
    from ._models import DataBoxDiskJobDetails  # type: ignore
    from ._models import DataBoxDiskJobSecrets  # type: ignore
    from ._models import DataBoxHeavyAccountCopyLogDetails  # type: ignore
    from ._models import DataBoxHeavyJobDetails  # type: ignore
    from ._models import DataBoxHeavyJobSecrets  # type: ignore
    from ._models import DataBoxHeavySecret  # type: ignore
    from ._models import DataBoxJobDetails  # type: ignore
    from ._models import DataBoxScheduleAvailabilityRequest  # type: ignore
    from ._models import DataBoxSecret  # type: ignore
    from ._models import DataDestinationDetailsValidationRequest  # type: ignore
    from ._models import DataDestinationDetailsValidationResponseProperties  # type: ignore
    from ._models import DataboxJobSecrets  # type: ignore
    from ._models import DcAccessSecurityCode  # type: ignore
    from ._models import DestinationAccountDetails  # type: ignore
    from ._models import DestinationManagedDiskDetails  # type: ignore
    from ._models import DestinationStorageAccountDetails  # type: ignore
    from ._models import DestinationToServiceLocationMap  # type: ignore
    from ._models import DiskScheduleAvailabilityRequest  # type: ignore
    from ._models import DiskSecret  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import HeavyScheduleAvailabilityRequest  # type: ignore
    from ._models import JobDeliveryInfo  # type: ignore
    from ._models import JobDetails  # type: ignore
    from ._models import JobErrorDetails  # type: ignore
    from ._models import JobResource  # type: ignore
    from ._models import JobResourceList  # type: ignore
    from ._models import JobResourceUpdateParameter  # type: ignore
    from ._models import JobSecrets  # type: ignore
    from ._models import JobStages  # type: ignore
    from ._models import NotificationPreference  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import PackageShippingDetails  # type: ignore
    from ._models import Preferences  # type: ignore
    from ._models import PreferencesValidationRequest  # type: ignore
    from ._models import PreferencesValidationResponseProperties  # type: ignore
    from ._models import RegionConfigurationRequest  # type: ignore
    from ._models import RegionConfigurationResponse  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ScheduleAvailabilityRequest  # type: ignore
    from ._models import ScheduleAvailabilityResponse  # type: ignore
    from ._models import ShareCredentialDetails  # type: ignore
    from ._models import ShipmentPickUpRequest  # type: ignore
    from ._models import ShipmentPickUpResponse  # type: ignore
    from ._models import ShippingAddress  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuAvailabilityValidationRequest  # type: ignore
    from ._models import SkuAvailabilityValidationResponseProperties  # type: ignore
    from ._models import SkuCapacity  # type: ignore
    from ._models import SkuCost  # type: ignore
    from ._models import SkuInformation  # type: ignore
    from ._models import SubscriptionIsAllowedToCreateJobValidationRequest  # type: ignore
    from ._models import SubscriptionIsAllowedToCreateJobValidationResponseProperties  # type: ignore
    from ._models import TransportAvailabilityDetails  # type: ignore
    from ._models import TransportAvailabilityRequest  # type: ignore
    from ._models import TransportAvailabilityResponse  # type: ignore
    from ._models import TransportPreferences  # type: ignore
    from ._models import UnencryptedCredentials  # type: ignore
    from ._models import UnencryptedCredentialsList  # type: ignore
    from ._models import UpdateJobDetails  # type: ignore
    from ._models import ValidateAddress  # type: ignore
    from ._models import ValidationInputRequest  # type: ignore
    from ._models import ValidationInputResponse  # type: ignore
    from ._models import ValidationRequest  # type: ignore
    from ._models import ValidationResponse  # type: ignore

from ._data_box_management_client_enums import (
    AccessProtocol,
    AddressType,
    AddressValidationStatus,
    ClassDiscriminator,
    CopyStatus,
    DataDestinationType,
    JobDeliveryType,
    NotificationStageName,
    OverallValidationStatus,
    ShareDestinationFormatType,
    SkuDisabledReason,
    SkuName,
    StageName,
    StageStatus,
    TransportShipmentTypes,
    ValidationInputDiscriminator,
    ValidationStatus,
)

__all__ = [
    'AccountCredentialDetails',
    'AddressValidationOutput',
    'AddressValidationProperties',
    'ApplianceNetworkConfiguration',
    'ArmBaseObject',
    'AvailableSkuRequest',
    'AvailableSkusResult',
    'CancellationReason',
    'CloudError',
    'ContactDetails',
    'CopyLogDetails',
    'CopyProgress',
    'CreateJobValidations',
    'CreateOrderLimitForSubscriptionValidationRequest',
    'CreateOrderLimitForSubscriptionValidationResponseProperties',
    'DataBoxAccountCopyLogDetails',
    'DataBoxDiskCopyLogDetails',
    'DataBoxDiskCopyProgress',
    'DataBoxDiskJobDetails',
    'DataBoxDiskJobSecrets',
    'DataBoxHeavyAccountCopyLogDetails',
    'DataBoxHeavyJobDetails',
    'DataBoxHeavyJobSecrets',
    'DataBoxHeavySecret',
    'DataBoxJobDetails',
    'DataBoxScheduleAvailabilityRequest',
    'DataBoxSecret',
    'DataDestinationDetailsValidationRequest',
    'DataDestinationDetailsValidationResponseProperties',
    'DataboxJobSecrets',
    'DcAccessSecurityCode',
    'DestinationAccountDetails',
    'DestinationManagedDiskDetails',
    'DestinationStorageAccountDetails',
    'DestinationToServiceLocationMap',
    'DiskScheduleAvailabilityRequest',
    'DiskSecret',
    'Error',
    'HeavyScheduleAvailabilityRequest',
    'JobDeliveryInfo',
    'JobDetails',
    'JobErrorDetails',
    'JobResource',
    'JobResourceList',
    'JobResourceUpdateParameter',
    'JobSecrets',
    'JobStages',
    'NotificationPreference',
    'Operation',
    'OperationDisplay',
    'OperationList',
    'PackageShippingDetails',
    'Preferences',
    'PreferencesValidationRequest',
    'PreferencesValidationResponseProperties',
    'RegionConfigurationRequest',
    'RegionConfigurationResponse',
    'Resource',
    'ScheduleAvailabilityRequest',
    'ScheduleAvailabilityResponse',
    'ShareCredentialDetails',
    'ShipmentPickUpRequest',
    'ShipmentPickUpResponse',
    'ShippingAddress',
    'Sku',
    'SkuAvailabilityValidationRequest',
    'SkuAvailabilityValidationResponseProperties',
    'SkuCapacity',
    'SkuCost',
    'SkuInformation',
    'SubscriptionIsAllowedToCreateJobValidationRequest',
    'SubscriptionIsAllowedToCreateJobValidationResponseProperties',
    'TransportAvailabilityDetails',
    'TransportAvailabilityRequest',
    'TransportAvailabilityResponse',
    'TransportPreferences',
    'UnencryptedCredentials',
    'UnencryptedCredentialsList',
    'UpdateJobDetails',
    'ValidateAddress',
    'ValidationInputRequest',
    'ValidationInputResponse',
    'ValidationRequest',
    'ValidationResponse',
    'AccessProtocol',
    'AddressType',
    'AddressValidationStatus',
    'ClassDiscriminator',
    'CopyStatus',
    'DataDestinationType',
    'JobDeliveryType',
    'NotificationStageName',
    'OverallValidationStatus',
    'ShareDestinationFormatType',
    'SkuDisabledReason',
    'SkuName',
    'StageName',
    'StageStatus',
    'TransportShipmentTypes',
    'ValidationInputDiscriminator',
    'ValidationStatus',
]
