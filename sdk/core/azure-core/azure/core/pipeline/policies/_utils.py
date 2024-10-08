# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import datetime
import email.utils
from typing import Optional, cast, Union, Tuple
from urllib.parse import urlparse

from azure.core.pipeline.transport import (
    HttpResponse as LegacyHttpResponse,
    AsyncHttpResponse as LegacyAsyncHttpResponse,
    HttpRequest as LegacyHttpRequest,
)
from azure.core.rest import HttpResponse, AsyncHttpResponse, HttpRequest


from ...utils._utils import _FixedOffset, case_insensitive_dict
from .. import PipelineResponse

AllHttpResponseType = Union[HttpResponse, LegacyHttpResponse, AsyncHttpResponse, LegacyAsyncHttpResponse]
HTTPRequestType = Union[HttpRequest, LegacyHttpRequest]


def _parse_http_date(text: str) -> datetime.datetime:
    """Parse a HTTP date format into datetime.

    :param str text: Text containing a date in HTTP format
    :rtype: datetime.datetime
    :return: The parsed datetime
    """
    parsed_date = email.utils.parsedate_tz(text)
    if not parsed_date:
        raise ValueError("Invalid HTTP date")
    tz_offset = cast(int, parsed_date[9])  # Look at the code, tz_offset is always an int, at worst 0
    return datetime.datetime(*parsed_date[:6], tzinfo=_FixedOffset(tz_offset / 60))


def parse_retry_after(retry_after: str) -> float:
    """Helper to parse Retry-After and get value in seconds.

    :param str retry_after: Retry-After header
    :rtype: float
    :return: Value of Retry-After in seconds.
    """
    delay: float  # Using the Mypy recommendation to use float for "int or float"
    try:
        delay = float(retry_after)
    except ValueError:
        # Not an integer? Try HTTP date
        retry_date = _parse_http_date(retry_after)
        delay = (retry_date - datetime.datetime.now(retry_date.tzinfo)).total_seconds()
    return max(0, delay)


def get_retry_after(response: PipelineResponse[HTTPRequestType, AllHttpResponseType]) -> Optional[float]:
    """Get the value of Retry-After in seconds.

    :param response: The PipelineResponse object
    :type response: ~azure.core.pipeline.PipelineResponse
    :return: Value of Retry-After in seconds.
    :rtype: float or None
    """
    headers = case_insensitive_dict(response.http_response.headers)
    retry_after = headers.get("retry-after")
    if retry_after:
        return parse_retry_after(retry_after)
    for ms_header in ["retry-after-ms", "x-ms-retry-after-ms"]:
        retry_after = headers.get(ms_header)
        if retry_after:
            parsed_retry_after = parse_retry_after(retry_after)
            return parsed_retry_after / 1000.0
    return None


def get_domain(url: str) -> str:
    """Get the domain of an url.

    :param str url: The url.
    :rtype: str
    :return: The domain of the url.
    """
    return str(urlparse(url).netloc).lower()


def get_challenge_parameter(headers, challenge_scheme: str, challenge_parameter: str) -> Optional[str]:
    """
    Parses the specified parameter from a challenge header found in the response.

    :param dict[str, str] headers: The response headers to parse.
    :param str challenge_scheme: The challenge scheme containing the challenge parameter, e.g., "Bearer".
    :param str challenge_parameter: The parameter key name to search for.
    :return: The value of the parameter name if found.
    :rtype: str or None
    """
    header_value = headers.get("WWW-Authenticate")
    if not header_value:
        return None

    scheme = challenge_scheme
    parameter = challenge_parameter
    header_span = header_value

    # Iterate through each challenge value.
    while True:
        challenge = get_next_challenge(header_span)
        if not challenge:
            break
        challenge_key, header_span = challenge
        if challenge_key.lower() != scheme.lower():
            continue
        # Enumerate each key-value parameter until we find the parameter key on the specified scheme challenge.
        while True:
            parameters = get_next_parameter(header_span)
            if not parameters:
                break
            key, value, header_span = parameters
            if key.lower() == parameter.lower():
                return value

    return None


def get_next_challenge(header_value: str) -> Optional[Tuple[str, str]]:
    """
    Iterates through the challenge schemes present in a challenge header.

    :param str header_value: The header value which will be sliced to remove the first parsed challenge key.
    :return: The parsed challenge scheme and the remaining header value.
    :rtype: tuple[str, str] or None
    """
    header_value = header_value.lstrip(" ")
    end_of_challenge_key = header_value.find(" ")

    if end_of_challenge_key < 0:
        return None

    challenge_key = header_value[:end_of_challenge_key]
    header_value = header_value[end_of_challenge_key + 1 :]

    return challenge_key, header_value


def get_next_parameter(header_value: str, separator: str = "=") -> Optional[Tuple[str, str, str]]:
    """
    Iterates through a challenge header value to extract key-value parameters.

    :param str header_value: The header value after being parsed by get_next_challenge.
    :param str separator: The challenge parameter key-value pair separator, default is '='.
    :return: The next available challenge parameter as a tuple (param_key, param_value, remaining header_value).
    :rtype: tuple[str, str, str] or None
    """
    space_or_comma = " ,"
    header_value = header_value.lstrip(space_or_comma)

    next_space = header_value.find(" ")
    next_separator = header_value.find(separator)

    if next_space < next_separator and next_space != -1:
        return None

    if next_separator < 0:
        return None

    param_key = header_value[:next_separator].strip()
    header_value = header_value[next_separator + 1 :]

    quote_index = header_value.find('"')

    if quote_index >= 0:
        header_value = header_value[quote_index + 1 :]
        param_value = header_value[: header_value.find('"')]
    else:
        trailing_delimiter_index = header_value.find(" ")
        if trailing_delimiter_index >= 0:
            param_value = header_value[:trailing_delimiter_index]
        else:
            param_value = header_value

    if header_value != param_value:
        header_value = header_value[len(param_value) + 1 :]

    return param_key, param_value, header_value
