# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.5, generator: @autorest/python@6.4.11)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

VERSION = "unknown"


class SearchIndexClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for SearchIndexClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: The endpoint URL of the search service. Required.
    :type endpoint: str
    :param index_name: The name of the index. Required.
    :type index_name: str
    :keyword api_version: Api Version. Default value is "2023-07-01-Preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, endpoint: str, index_name: str, **kwargs: Any) -> None:
        super(SearchIndexClientConfiguration, self).__init__(**kwargs)
        api_version: str = kwargs.pop("api_version", "2023-07-01-Preview")

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if index_name is None:
            raise ValueError("Parameter 'index_name' must not be None.")

        self.endpoint = endpoint
        self.index_name = index_name
        self.api_version = api_version
        kwargs.setdefault("sdk_moniker", "searchindexclient/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
