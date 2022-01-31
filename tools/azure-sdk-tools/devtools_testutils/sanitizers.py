# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import requests
import sys
from typing import TYPE_CHECKING

from .config import PROXY_URL
from .helpers import is_live_and_not_recording

if TYPE_CHECKING:
    from typing import Any, Dict

# We store session-level sanitizers and matchers in a module variable. Any settings at the "session" level (read, not at the recording Id) are not added until
# a recording has been started. When that occurs, any session level sanitizers/matchers are then applied to the recording id returned from the test-proxy Start operation.
this = sys.modules[__name__]
this.global_sanitizers = []
this.global_matchers = []


def set_bodiless_matcher(recording_id=None):
    # type: (str) -> None
    """Adjusts the "match" operation to EXCLUDE the body when matching a request to a recording's entries.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    """

    if recording_id:
        _send_matcher_request("BodilessMatcher", {"x-recording-id": recording_id})
    else:
        this.global_matchers.append(("BodilessMatcher", {}))


def add_body_key_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that offers regex update of a specific JTokenPath within a returned body.

    For example, "TableName" within a json response body having its value replaced by whatever substitution is offered.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str json_path: The SelectToken path (which could possibly match multiple entries) that will be used to
        select JTokens for value replacement.
    :keyword str value: The substitution value.
    :keyword str regex: A regex. Can be defined as a simple regex replace OR if groupForReplace is set, a subsitution
        operation. Defaults to replacing the entire string.
    :keyword str group_for_replace: The capture group that needs to be operated upon. Do not provide if you're invoking
        a simple replacement operation.
    """

    request_args = _get_request_args(**kwargs)

    if recording_id:
        _send_sanitizer_request("BodyKeySanitizer", recording_id, request_args)
    else:
        this.global_sanitizers.append(("BodyKeySanitizer", request_args))


def add_body_regex_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that offers regex replace within a returned body.

    Specifically, this means regex applying to the raw JSON. If you are attempting to simply replace a specific key, the
    BodyKeySanitizer is probably the way to go.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str value: The substitution value.
    :keyword str regex: A regex. Can be defined as a simple regex, or if a ``group_for_replace`` is provided, a
        substitution operation.
    :keyword str group_for_replace: The capture group that needs to be operated upon. Do not provide if you're invoking
        a simple replacement operation.
    """

    request_args = _get_request_args(**kwargs)

    if recording_id:
        _send_sanitizer_request("BodyRegexSanitizer", recording_id, request_args)
    else:
        this.global_sanitizers.append(("BodyRegexSanitizer", request_args))


def add_continuation_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that's used to anonymize private keys in response/request pairs.

    For instance, a request hands back a "sessionId" that needs to be present in the next request. Supports "all further
    requests get this key" as well as "single response/request pair". Defaults to maintaining same key for rest of
    recording.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str key: The name of the header whos value will be replaced from response -> next request.
    :keyword str method: The method by which the value of the targeted key will be replaced. Defaults to guid
        replacement.
    :keyword str reset_after_first: Do we need multiple pairs replaced? Or do we want to replace each value with the
        same value?
    """

    request_args = _get_request_args(**kwargs)

    if recording_id:
        _send_sanitizer_request("ContinuationSanitizer", recording_id, request_args)
    else:
        this.global_sanitizers.append(("ContinuationSanitizer", request_args))


def add_general_regex_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that offers a general regex replace across request/response Body, Headers, and URI.

    For the body, this means regex applying to the raw JSON.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str value: The substitution value.
    :keyword str regex: A regex. Can be defined as a simple regex, or if a ``group_for_replace`` is provided, a
        substitution operation.
    :keyword str group_for_replace: The capture group that needs to be operated upon. Do not provide if you're invoking
        a simple replacement operation.
    """

    request_args = _get_request_args(**kwargs)

    if recording_id:
        _send_sanitizer_request("GeneralRegexSanitizer", recording_id, request_args)
    else:
        this.global_sanitizers.append(("GeneralRegexSanitizer", request_args))


def add_header_regex_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that offers regex replace on returned headers.

    Can be used for multiple purposes: 1) To replace a key with a specific value, do not set "regex" value. 2) To do a
    simple regex replace operation, define arguments "key", "value", and "regex". 3) To do a targeted substitution of a
    specific group, define all arguments "key", "value", and "regex".

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str key: The name of the header we're operating against.
    :keyword str value: The substitution or whole new header value, depending on "regex" setting.
    :keyword str regex: A regex. Can be defined as a simple regex, or if a ``group_for_replace`` is provided, a
        substitution operation.
    :keyword str group_for_replace: The capture group that needs to be operated upon. Do not provide if you're invoking
        a simple replacement operation.
    """

    request_args = _get_request_args(recording_id=None, **kwargs)

    if recording_id:
        _send_sanitizer_request("HeaderRegexSanitizer", recording_id, request_args)
    else:
        this.global_sanitizers.append(("HeaderRegexSanitizer", request_args))


def add_oauth_response_sanitizer(recording_id=None):
    # type: (str) -> None
    """Registers a sanitizer that cleans out all request/response pairs that match an oauth regex in their URI.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    """
    if recording_id:
        _send_sanitizer_request("OAuthResponseSanitizer", recording_id, {})
    else:
        this.global_sanitizers.append(("OAuthResponseSanitizer", recording_id, {}))


def add_remove_header_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that removes specified headers before saving a recording.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str headers: A comma separated list. Should look like "Location, Transfer-Encoding" or something along
        those lines. Don't worry about whitespace between the commas separating each key. They will be ignored.
    """

    request_args = _get_request_args(recording_id=None, **kwargs)

    if recording_id:
        _send_sanitizer_request("RemoveHeaderSanitizer", request_args)
    else:
        this.global_sanitizers.append(("RemoveHeaderSanitizer", request_args))


def add_request_subscription_id_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer that replaces subscription IDs in requests.

    Subscription IDs are replaced with "00000000-0000-0000-0000-000000000000" by default.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str value: The fake subscriptionId that will be placed where the real one is in the real request.
    """

    request_args = _get_request_args(**kwargs)

    if recording_id:
        _send_sanitizer_request("ReplaceRequestSubscriptionId", recording_id, request_args)
    else:
        this.global_sanitizers.append(("ReplaceRequestSubscriptionId", request_args))


def add_uri_regex_sanitizer(recording_id=None, **kwargs):
    # type: (str, **Any) -> None
    """Registers a sanitizer for cleaning URIs via regex.

    :param str recording_id: The targeted recording id this sanitizer will be added to. Absence of this param results in a deferred session-level sanitizer.
    :keyword str value: The substitution value.
    :keyword str regex: A regex. Can be defined as a simple regex, or if a ``group_for_replace`` is provided, a
        substitution operation.
    :keyword str group_for_replace: The capture group that needs to be operated upon. Do not provide if you're invoking
        a simple replacement operation.
    """

    request_args = _get_request_args(**kwargs)
    if recording_id:
        _send_sanitizer_request("UriRegexSanitizer", recording_id, request_args)
    else:
        this.global_sanitizers.append(("UriRegexSanitizer", request_args))


def set_recording_settings(recording_id):
    # type: (str) -> None
    """Applies all globally set sanitizers and matchers to an individual recording id.

    :param str recording_id: The targeted recording that these settings will be applied to. Retrieved from proxy_testcase.start_record_or_playback.
    """
    _send_deferred_sanitizers(recording_id)
    _send_deferred_matchers(recording_id)


def _send_deferred_sanitizers(recording_id):
    # type: (str) -> None
    """Sets session-set sanitizers to a specific recording.

    :param str recording_id: The targeted recording that these sanitizers will be applied to. Retrieved from proxy_testcase.start_record_or_playback.
    """
    for deferred_sanitizer_tuple in this.global_sanitizers:
        _send_sanitizer_request(deferred_sanitizer_tuple[0], recording_id, deferred_sanitizer_tuple[1])


def _send_deferred_matchers(recording_id):
    # type: (str) -> None
    """Sets session-set matchers to a specific recording. Given the nature of how the test-proxy handles a matcher. The last one sent will be the "winner"
    on test-proxy side.

    :param str recording_id: The targeted recording that these matchers will be applied to. Retrieved from proxy_testcase.start_record_or_playback.
    """
    for deferred_matcher_tuple in this.global_matchers:
        _send_matcher_request(deferred_matcher_tuple[0], recording_id, deferred_matcher_tuple[1])


def _get_request_args(**kwargs):
    # type: (**Any) -> Dict
    """Returns a dictionary of sanitizer constructor headers"""

    request_args = {}
    if "group_for_replace" in kwargs:
        request_args["groupForReplace"] = kwargs.get("group_for_replace")
    if "headers" in kwargs:
        request_args["headersForRemoval"] = kwargs.get("headers")
    if "json_path" in kwargs:
        request_args["jsonPath"] = kwargs.get("json_path")
    if "key" in kwargs:
        request_args["key"] = kwargs.get("key")
    if "method" in kwargs:
        request_args["method"] = kwargs.get("method")
    if "regex" in kwargs:
        request_args["regex"] = kwargs.get("regex")
    if "reset_after_first" in kwargs:
        request_args["resetAfterFirst"] = kwargs.get("reset_after_first")
    if "value" in kwargs:
        request_args["value"] = kwargs.get("value")
    return request_args


def _send_matcher_request(matcher, recording_id, headers):
    # type: (str, str, Dict) -> None
    """Sends a POST request to the test proxy endpoint to register the specified matcher.

    If live tests are being run with recording turned off via the AZURE_SKIP_LIVE_RECORDING environment variable, no
    request will be sent.

    :param str matcher: The name of the matcher to set.
    :param str recording_id: An individual recording id that this matcher is being set for.
    :param dict headers: Any matcher headers, as a dictionary.
    """

    if is_live_and_not_recording():
        return

    headers_to_send = {"x-abstraction-identifier": matcher}
    headers_to_send.update(headers)

    if recording_id:
        headers_to_send["x-recording-id"] = recording_id

    requests.post(
        "{}/Admin/SetMatcher".format(PROXY_URL),
        headers=headers_to_send,
    )


def _send_sanitizer_request(sanitizer, recording_id, parameters):
    # type: (str, str, Dict) -> None
    """Sends a POST request to the test proxy endpoint to register the specified sanitizer.

    If live tests are being run with recording turned off via the AZURE_SKIP_LIVE_RECORDING environment variable, no
    request will be sent.

    :param str sanitizer: The name of the sanitizer to add.
    :param str recording_id: An individual recording id that this matcher is being set for.
    :param dict parameters: The sanitizer constructor parameters, as a dictionary.
    """

    if is_live_and_not_recording():
        return

    headers_to_send = {"x-abstraction-identifier": sanitizer, "Content-Type": "application/json"}
    if recording_id:
        headers_to_send["x-recording-id"] = recording_id

    requests.post("{}/Admin/AddSanitizer".format(PROXY_URL), headers=headers_to_send, json=parameters)
