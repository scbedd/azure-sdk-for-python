import asyncio
import functools
from contextlib import contextmanager

from ..proxy_testcase import (
    get_test_id,
    start_record_or_playback,
    transform_request,
    stop_record_or_playback,
)

from azure.core.pipeline.transport import AioHttpTransport

from azure_devtools.scenario_tests.utilities import trim_kwargs_from_test_function

def RecordedByProxyAsync(func):
    async def record_wrap(*args, **kwargs):
        test_id = get_test_id()
        recording_id = start_record_or_playback(test_id)

        def transform_args(*args, **kwargs):
            copied_positional_args = list(args)
            request = copied_positional_args[1]

            # TODO, get the test-proxy server a real SSL certificate. The issue here is that SSL Certificates are
            # normally associated with a domain name. Need to talk to the //SSLAdmin folks (or someone else) and get
            # a recommendation for how to get a valid SSL Cert for localhost
            kwargs["connection_verify"] = False

            transform_request(request, recording_id)

            return tuple(copied_positional_args), kwargs

        trimmed_kwargs = {k: v for k, v in kwargs.items()}
        trim_kwargs_from_test_function(func, trimmed_kwargs)

        original_func = AioHttpTransport.send

        async def combined_call(*args, **kwargs):
            adjusted_args, adjusted_kwargs = transform_args(*args, **kwargs)
            req = adjusted_args[1]
            print("HEADERS: ", req.headers)
            print("BODY: ", req.body)
            print("METHOD: ", req.method)
            return await original_func(*adjusted_args, **adjusted_kwargs)

        AioHttpTransport.send = combined_call

        # call the modified function.
        try:
            value = await func(*args, **trimmed_kwargs)
        finally:
            AioHttpTransport.send = original_func
            stop_record_or_playback(test_id, recording_id)

        return value

    return record_wrap
