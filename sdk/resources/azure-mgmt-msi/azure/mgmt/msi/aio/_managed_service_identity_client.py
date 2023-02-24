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

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from .._serialization import Deserializer, Serializer
from ._configuration import ManagedServiceIdentityClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ManagedServiceIdentityClient(MultiApiClientMixin, _SDKClient):
    """The Managed Service Identity Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Id of the Subscription to which the identity belongs. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2023-01-31'
    _PROFILE_TAG = "azure.mgmt.msi.ManagedServiceIdentityClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        api_version: Optional[str] = None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs: Any
    ) -> None:
        self._config = ManagedServiceIdentityClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ManagedServiceIdentityClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2018-11-30: :mod:`v2018_11_30.models<azure.mgmt.msi.v2018_11_30.models>`
           * 2021-09-30-preview: :mod:`v2021_09_30_preview.models<azure.mgmt.msi.v2021_09_30_preview.models>`
           * 2022-01-31-preview: :mod:`v2022_01_31_preview.models<azure.mgmt.msi.v2022_01_31_preview.models>`
           * 2023-01-31: :mod:`v2023_01_31.models<azure.mgmt.msi.v2023_01_31.models>`
        """
        if api_version == '2018-11-30':
            from ..v2018_11_30 import models
            return models
        elif api_version == '2021-09-30-preview':
            from ..v2021_09_30_preview import models
            return models
        elif api_version == '2022-01-31-preview':
            from ..v2022_01_31_preview import models
            return models
        elif api_version == '2023-01-31':
            from ..v2023_01_31 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def federated_identity_credentials(self):
        """Instance depends on the API version:

           * 2022-01-31-preview: :class:`FederatedIdentityCredentialsOperations<azure.mgmt.msi.v2022_01_31_preview.aio.operations.FederatedIdentityCredentialsOperations>`
           * 2023-01-31: :class:`FederatedIdentityCredentialsOperations<azure.mgmt.msi.v2023_01_31.aio.operations.FederatedIdentityCredentialsOperations>`
        """
        api_version = self._get_api_version('federated_identity_credentials')
        if api_version == '2022-01-31-preview':
            from ..v2022_01_31_preview.aio.operations import FederatedIdentityCredentialsOperations as OperationClass
        elif api_version == '2023-01-31':
            from ..v2023_01_31.aio.operations import FederatedIdentityCredentialsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'federated_identity_credentials'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2018-11-30: :class:`Operations<azure.mgmt.msi.v2018_11_30.aio.operations.Operations>`
           * 2021-09-30-preview: :class:`Operations<azure.mgmt.msi.v2021_09_30_preview.aio.operations.Operations>`
           * 2022-01-31-preview: :class:`Operations<azure.mgmt.msi.v2022_01_31_preview.aio.operations.Operations>`
           * 2023-01-31: :class:`Operations<azure.mgmt.msi.v2023_01_31.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2018-11-30':
            from ..v2018_11_30.aio.operations import Operations as OperationClass
        elif api_version == '2021-09-30-preview':
            from ..v2021_09_30_preview.aio.operations import Operations as OperationClass
        elif api_version == '2022-01-31-preview':
            from ..v2022_01_31_preview.aio.operations import Operations as OperationClass
        elif api_version == '2023-01-31':
            from ..v2023_01_31.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def system_assigned_identities(self):
        """Instance depends on the API version:

           * 2018-11-30: :class:`SystemAssignedIdentitiesOperations<azure.mgmt.msi.v2018_11_30.aio.operations.SystemAssignedIdentitiesOperations>`
           * 2021-09-30-preview: :class:`SystemAssignedIdentitiesOperations<azure.mgmt.msi.v2021_09_30_preview.aio.operations.SystemAssignedIdentitiesOperations>`
           * 2022-01-31-preview: :class:`SystemAssignedIdentitiesOperations<azure.mgmt.msi.v2022_01_31_preview.aio.operations.SystemAssignedIdentitiesOperations>`
           * 2023-01-31: :class:`SystemAssignedIdentitiesOperations<azure.mgmt.msi.v2023_01_31.aio.operations.SystemAssignedIdentitiesOperations>`
        """
        api_version = self._get_api_version('system_assigned_identities')
        if api_version == '2018-11-30':
            from ..v2018_11_30.aio.operations import SystemAssignedIdentitiesOperations as OperationClass
        elif api_version == '2021-09-30-preview':
            from ..v2021_09_30_preview.aio.operations import SystemAssignedIdentitiesOperations as OperationClass
        elif api_version == '2022-01-31-preview':
            from ..v2022_01_31_preview.aio.operations import SystemAssignedIdentitiesOperations as OperationClass
        elif api_version == '2023-01-31':
            from ..v2023_01_31.aio.operations import SystemAssignedIdentitiesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'system_assigned_identities'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def user_assigned_identities(self):
        """Instance depends on the API version:

           * 2018-11-30: :class:`UserAssignedIdentitiesOperations<azure.mgmt.msi.v2018_11_30.aio.operations.UserAssignedIdentitiesOperations>`
           * 2021-09-30-preview: :class:`UserAssignedIdentitiesOperations<azure.mgmt.msi.v2021_09_30_preview.aio.operations.UserAssignedIdentitiesOperations>`
           * 2022-01-31-preview: :class:`UserAssignedIdentitiesOperations<azure.mgmt.msi.v2022_01_31_preview.aio.operations.UserAssignedIdentitiesOperations>`
           * 2023-01-31: :class:`UserAssignedIdentitiesOperations<azure.mgmt.msi.v2023_01_31.aio.operations.UserAssignedIdentitiesOperations>`
        """
        api_version = self._get_api_version('user_assigned_identities')
        if api_version == '2018-11-30':
            from ..v2018_11_30.aio.operations import UserAssignedIdentitiesOperations as OperationClass
        elif api_version == '2021-09-30-preview':
            from ..v2021_09_30_preview.aio.operations import UserAssignedIdentitiesOperations as OperationClass
        elif api_version == '2022-01-31-preview':
            from ..v2022_01_31_preview.aio.operations import UserAssignedIdentitiesOperations as OperationClass
        elif api_version == '2023-01-31':
            from ..v2023_01_31.aio.operations import UserAssignedIdentitiesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'user_assigned_identities'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
