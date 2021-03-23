# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools
import inspect
import logging
import os.path
import sys
import time
import zlib
import pdb

from azure.core.pipeline.transport import RequestsTransport, AsyncioRequestsTransport

try:
    from inspect import getfullargspec as get_arg_spec
except ImportError:
    from inspect import getargspec as get_arg_spec

import pytest
from azure_devtools.scenario_tests.utilities import trim_kwargs_from_test_function

from .config import TEST_SETTING_FILENAME
from . import mgmt_settings_fake as fake_settings

import requests
from contextlib import contextmanager

PROXY_URL = "https://localhost:5001"
RECORDING_START_URL = "{}/record/start".format(PROXY_URL)
RECORDING_STOP_URL = "{}/record/stop".format(PROXY_URL)
PLAYBACK_START_URL = "{}/playback/start".format(PROXY_URL)
PLAYBACK_STOP_URL = "{}/playback/stop".format(PROXY_URL)
TEST_FILE_FORMAT = "recordings/{}.txt"

def write_recording_id(test_id, recording_id):
    try:
        os.makedirs("recordings")
    except:
        pass

    with open(TEST_FILE_FORMAT.format(test_id), "w") as f:
        f.write(recording_id)


def get_recording_id(test_id):
    with open(TEST_FILE_FORMAT.format(test_id), "r") as f:
        result = f.readline()

    return result.strip()

@contextmanager
def patch_requests_func(request_transform):
    original_func = RequestsTransport.send

    def combined_call(*args, **kwargs):
        adjusted_args, adjusted_kwargs = request_transform(*args,**kwargs)
        return original_func(*adjusted_args, **adjusted_kwargs)
        
    RequestsTransport.send = combined_call
    yield None

    RequestsTransport.send = original_func

def RecordedByProxy(func):
    @functools.wraps(func)
    def record_wrap(*args, **kwargs):
        recording_id = ""
        test_id = func.__name__

        if os.getenv("AZURE_RECORD_MODE") == "record":
            result = requests.post(
                RECORDING_START_URL, headers={"x-recording-file": test_id}, verify=False
            )
            recording_id = result.headers["x-recording-id"]
        elif os.getenv("AZURE_RECORD_MODE") == "playback":
            result = requests.post(
                PLAYBACK_START_URL,
                headers={"x-recording-file": test_id, "x-recording-id": recording_id},
                verify=False,
            )
            recording_id = get_recording_id(test_id)

        def transform_args(*args, **kwargs):
            copied_positional_args = list(args)
            request = copied_positional_args[1]
            upstream_url = request.url.replace("//text", "/text")
            headers = request.headers
            
            kwargs["connection_verify"] = False

            # in recording, we want to forward the request with record mode of record
            if os.getenv("AZURE_RECORD_MODE") == "record":
                headers["x-recording-upstream-base-uri"] = upstream_url
                headers["x-recording-id"] = recording_id
                headers["x-recording-mode"] = "record"
                request.url = PROXY_URL

            # otherwise we want to forward the request with record mode of playback
            elif os.getenv("AZURE_RECORD_MODE") == "playback":
                headers["x-recording-upstream-base-uri"] = upstream_url
                headers["x-recording-id"] = recording_id
                headers["x-recording-mode"] = "playback"
                request.url = PROXY_URL

            return tuple(copied_positional_args), kwargs

        trimmed_kwargs = {k:v for k,v in kwargs.items()}
        trim_kwargs_from_test_function(func, trimmed_kwargs)

        # this ensures that within this scope, we've monkeypatched the send functionality
        with patch_requests_func(transform_args):
            # call the modified function.
            value = func(*args, **trimmed_kwargs)
           
        if os.getenv("AZURE_RECORD_MODE") == "record":
            result = requests.post(
                RECORDING_STOP_URL,
                headers={"x-recording-file": test_id, "x-recording-id": recording_id, "x-recording-save": "true"},
                verify=False,
            )
            write_recording_id(test_id, recording_id)
        elif os.getenv("AZURE_RECORD_MODE") == "playback":
            result = requests.post(
                PLAYBACK_STOP_URL,
                headers={"x-recording-file": test_id, "x-recording-id": recording_id},
                verify=False,
            )

        return value

    return record_wrap
