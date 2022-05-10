# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_request(
    subscription_id: str,
    location_name: str,
    target_type_name: str,
    *,
    continuation_token_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-09-15-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'),
        "locationName": _SERIALIZER.url("location_name", location_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
        "targetTypeName": _SERIALIZER.url("target_type_name", target_type_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if continuation_token_parameter is not None:
        _query_parameters['continuationToken'] = _SERIALIZER.query("continuation_token_parameter", continuation_token_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_request(
    subscription_id: str,
    location_name: str,
    target_type_name: str,
    capability_type_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-09-15-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes/{capabilityTypeName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'),
        "locationName": _SERIALIZER.url("location_name", location_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
        "targetTypeName": _SERIALIZER.url("target_type_name", target_type_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
        "capabilityTypeName": _SERIALIZER.url("capability_type_name", capability_type_name, 'str', pattern=r'^[a-zA-Z0-9\-\.]+-\d\.\d$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

class CapabilityTypesOperations(object):
    """CapabilityTypesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.chaos.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        location_name: str,
        target_type_name: str,
        continuation_token_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.CapabilityTypeListResult"]:
        """Get a list of Capability Type resources for given Target Type and location.

        :param location_name: String that represents a Location resource name.
        :type location_name: str
        :param target_type_name: String that represents a Target Type resource name.
        :type target_type_name: str
        :param continuation_token_parameter: String that sets the continuation token. Default value is
         None.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CapabilityTypeListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.chaos.models.CapabilityTypeListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-09-15-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CapabilityTypeListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    location_name=location_name,
                    target_type_name=target_type_name,
                    api_version=api_version,
                    continuation_token_parameter=continuation_token_parameter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    location_name=location_name,
                    target_type_name=target_type_name,
                    api_version=api_version,
                    continuation_token_parameter=continuation_token_parameter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("CapabilityTypeListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes"}  # type: ignore

    @distributed_trace
    def get(
        self,
        location_name: str,
        target_type_name: str,
        capability_type_name: str,
        **kwargs: Any
    ) -> "_models.CapabilityType":
        """Get a Capability Type resource for given Target Type and location.

        :param location_name: String that represents a Location resource name.
        :type location_name: str
        :param target_type_name: String that represents a Target Type resource name.
        :type target_type_name: str
        :param capability_type_name: String that represents a Capability Type resource name.
        :type capability_type_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapabilityType, or the result of cls(response)
        :rtype: ~azure.mgmt.chaos.models.CapabilityType
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CapabilityType"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-09-15-preview")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            location_name=location_name,
            target_type_name=target_type_name,
            capability_type_name=capability_type_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CapabilityType', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes/{capabilityTypeName}"}  # type: ignore

