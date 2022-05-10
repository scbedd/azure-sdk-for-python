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
    vault_name: str,
    resource_group_name: str,
    subscription_id: str,
    fabric_name: str,
    container_name: str,
    protected_item_name: str,
    *,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints")  # pylint: disable=line-too-long
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
        "protectedItemName": _SERIALIZER.url("protected_item_name", protected_item_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if filter is not None:
        _query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')

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
    vault_name: str,
    resource_group_name: str,
    subscription_id: str,
    fabric_name: str,
    container_name: str,
    protected_item_name: str,
    recovery_point_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
        "protectedItemName": _SERIALIZER.url("protected_item_name", protected_item_name, 'str'),
        "recoveryPointId": _SERIALIZER.url("recovery_point_id", recovery_point_id, 'str'),
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

class RecoveryPointsOperations(object):
    """RecoveryPointsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.recoveryservicesbackup.activestamp.models
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
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.RecoveryPointResourceList"]:
        """Lists the backup copies for the backed up item.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up item.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up item.
        :type container_name: str
        :param protected_item_name: Backed up item whose backup copies are to be fetched.
        :type protected_item_name: str
        :param filter: OData filter options. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RecoveryPointResourceList or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.recoveryservicesbackup.activestamp.models.RecoveryPointResourceList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-12-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RecoveryPointResourceList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    vault_name=vault_name,
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    fabric_name=fabric_name,
                    container_name=container_name,
                    protected_item_name=protected_item_name,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    vault_name=vault_name,
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    fabric_name=fabric_name,
                    container_name=container_name,
                    protected_item_name=protected_item_name,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RecoveryPointResourceList", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints"}  # type: ignore

    @distributed_trace
    def get(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        **kwargs: Any
    ) -> "_models.RecoveryPointResource":
        """Provides the information of the backed up data identified using RecoveryPointID. This is an
        asynchronous operation.
        To know the status of the operation, call the GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with backed up item.
        :type fabric_name: str
        :param container_name: Container name associated with backed up item.
        :type container_name: str
        :param protected_item_name: Backed up item name whose backup data needs to be fetched.
        :type protected_item_name: str
        :param recovery_point_id: RecoveryPointID represents the backed up data to be fetched.
        :type recovery_point_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RecoveryPointResource, or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.RecoveryPointResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RecoveryPointResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-12-01")  # type: str

        
        request = build_get_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            recovery_point_id=recovery_point_id,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RecoveryPointResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}"}  # type: ignore

