# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ResourceHealthMgmtClientConfiguration
from .operations import (
    AvailabilityStatusesOperations,
    ChildAvailabilityStatusesOperations,
    ChildResourcesOperations,
    EmergingIssuesOperations,
    EventOperations,
    EventsOperations,
    ImpactedResourcesOperations,
    MetadataOperations,
    Operations,
    SecurityAdvisoryImpactedResourcesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ResourceHealthMgmtClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Resource Health Client.

    :ivar availability_statuses: AvailabilityStatusesOperations operations
    :vartype availability_statuses:
     azure.mgmt.resourcehealth.v2023_10_01_preview.operations.AvailabilityStatusesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resourcehealth.v2023_10_01_preview.operations.Operations
    :ivar metadata: MetadataOperations operations
    :vartype metadata: azure.mgmt.resourcehealth.v2023_10_01_preview.operations.MetadataOperations
    :ivar impacted_resources: ImpactedResourcesOperations operations
    :vartype impacted_resources:
     azure.mgmt.resourcehealth.v2023_10_01_preview.operations.ImpactedResourcesOperations
    :ivar security_advisory_impacted_resources: SecurityAdvisoryImpactedResourcesOperations
     operations
    :vartype security_advisory_impacted_resources:
     azure.mgmt.resourcehealth.v2023_10_01_preview.operations.SecurityAdvisoryImpactedResourcesOperations
    :ivar events: EventsOperations operations
    :vartype events: azure.mgmt.resourcehealth.v2023_10_01_preview.operations.EventsOperations
    :ivar event: EventOperations operations
    :vartype event: azure.mgmt.resourcehealth.v2023_10_01_preview.operations.EventOperations
    :ivar child_availability_statuses: ChildAvailabilityStatusesOperations operations
    :vartype child_availability_statuses:
     azure.mgmt.resourcehealth.v2023_10_01_preview.operations.ChildAvailabilityStatusesOperations
    :ivar child_resources: ChildResourcesOperations operations
    :vartype child_resources:
     azure.mgmt.resourcehealth.v2023_10_01_preview.operations.ChildResourcesOperations
    :ivar emerging_issues: EmergingIssuesOperations operations
    :vartype emerging_issues:
     azure.mgmt.resourcehealth.v2023_10_01_preview.operations.EmergingIssuesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-10-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ResourceHealthMgmtClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.availability_statuses = AvailabilityStatusesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.metadata = MetadataOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.impacted_resources = ImpactedResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.security_advisory_impacted_resources = SecurityAdvisoryImpactedResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.events = EventsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.event = EventOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.child_availability_statuses = ChildAvailabilityStatusesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.child_resources = ChildResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )
        self.emerging_issues = EmergingIssuesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-01-preview"
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ResourceHealthMgmtClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
