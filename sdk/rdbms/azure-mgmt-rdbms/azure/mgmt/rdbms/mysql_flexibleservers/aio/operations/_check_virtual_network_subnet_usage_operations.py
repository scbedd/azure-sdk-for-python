# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._check_virtual_network_subnet_usage_operations import build_execute_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CheckVirtualNetworkSubnetUsageOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.rdbms.mysql_flexibleservers.aio.MySQLManagementClient`'s
        :attr:`check_virtual_network_subnet_usage` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def execute(
        self,
        location_name: str,
        parameters: _models.VirtualNetworkSubnetUsageParameter,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.VirtualNetworkSubnetUsageResult:
        """Get virtual network subnet usage for a given vNet resource id.

        :param location_name: The name of the location. Required.
        :type location_name: str
        :param parameters: The required parameters for creating or updating a server. Required.
        :type parameters:
         ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageParameter
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VirtualNetworkSubnetUsageResult or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def execute(
        self, location_name: str, parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VirtualNetworkSubnetUsageResult:
        """Get virtual network subnet usage for a given vNet resource id.

        :param location_name: The name of the location. Required.
        :type location_name: str
        :param parameters: The required parameters for creating or updating a server. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VirtualNetworkSubnetUsageResult or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def execute(
        self,
        location_name: str,
        parameters: Union[_models.VirtualNetworkSubnetUsageParameter, IO[bytes]],
        **kwargs: Any
    ) -> _models.VirtualNetworkSubnetUsageResult:
        """Get virtual network subnet usage for a given vNet resource id.

        :param location_name: The name of the location. Required.
        :type location_name: str
        :param parameters: The required parameters for creating or updating a server. Is either a
         VirtualNetworkSubnetUsageParameter type or a IO[bytes] type. Required.
        :type parameters:
         ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageParameter or IO[bytes]
        :return: VirtualNetworkSubnetUsageResult or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-30"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.VirtualNetworkSubnetUsageResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "VirtualNetworkSubnetUsageParameter")

        _request = build_execute_request(
            location_name=location_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualNetworkSubnetUsageResult", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
