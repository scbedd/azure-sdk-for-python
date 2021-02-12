# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
import unittest
import os
import inspect
import tempfile
import shutil
import logging
import threading
import six
import vcr

from .config import TestConfig
from .const import ENV_TEST_DIAGNOSE
from .utilities import create_random_name
from .decorators import live_only
from .base import IntegrationTestBase, LiveTest


class ProxiedTest(IntegrationTestBase):  # pylint: disable=too-many-instance-attributes
    FILTER_HEADERS = [
        'authorization',
        'client-request-id',
        'retry-after',
        'x-ms-client-request-id',
        'x-ms-correlation-request-id',
        'x-ms-ratelimit-remaining-subscription-reads',
        'x-ms-request-id',
        'x-ms-routing-request-id',
        'x-ms-gateway-service-instanceid',
        'x-ms-ratelimit-remaining-tenant-reads',
        'x-ms-served-by',
        'x-ms-authorization-auxiliary'
    ]

    def __init__(self,  # pylint: disable=too-many-arguments
                 method_name, config_file=None, recording_dir=None, recording_name=None, recording_processors=None,
                 replay_processors=None, recording_patches=None, replay_patches=None, match_body=False,
                 custom_request_matchers=None):
        super(ProxiedTest, self).__init__(method_name)


        self.test_resources_count = 0
        self.is_live = 'true'
        self.original_env = os.environ.copy()

    def setUp(self):
        super(ProxiedTest, self).setUp()

        if self.is_live and os.environ.get('AZURE_SKIP_LIVE_RECORDING', '').lower() == 'true':
            return

    def tearDown(self):
        os.environ = self.original_env
        # Autorest.Python 2.x
        assert not [t for t in threading.enumerate() if t.name.startswith("AzureOperationPoller")], \
            "You need to call 'result' or 'wait' on all AzureOperationPoller you have created"
        # Autorest.Python 3.x
        assert not [t for t in threading.enumerate() if t.name.startswith("LROPoller")], \
            "You need to call 'result' or 'wait' on all LROPoller you have created"

    def _process_request_recording(self, request):
        if self.disable_recording:
            return None

        if self.in_recording:
            for processor in self.recording_processors:
                request = processor.process_request(request)
                if not request:
                    break
        else:
            for processor in self.replay_processors:
                request = processor.process_request(request)
                if not request:
                    break

        return request

    def _process_response_recording(self, response):
        from .utilities import is_text_payload
        if self.in_recording:
            # make header name lower case and filter unwanted headers
            headers = {}
            for key in response['headers']:
                if key.lower() not in self.FILTER_HEADERS:
                    headers[key.lower()] = response['headers'][key]
            response['headers'] = headers

            body = response['body']['string']
            if is_text_payload(response) and body and not isinstance(body, six.string_types):
                response['body']['string'] = body.decode('utf-8')

            for processor in self.recording_processors:
                response = processor.process_response(response)
                if not response:
                    break
        else:
            for processor in self.replay_processors:
                response = processor.process_response(response)
                if not response:
                    break

        return response

    @classmethod
    def _custom_request_query_matcher(cls, r1, r2):
        """ Ensure method, path, and query parameters match. """
        from six.moves.urllib_parse import urlparse, parse_qs  # pylint: disable=import-error,relative-import

        url1 = urlparse(r1.uri)
        url2 = urlparse(r2.uri)

        q1 = parse_qs(url1.query)
        q2 = parse_qs(url2.query)
        shared_keys = set(q1.keys()).intersection(set(q2.keys()))

        if len(shared_keys) != len(q1) or len(shared_keys) != len(q2):
            return False

        for key in shared_keys:
            if q1[key][0].lower() != q2[key][0].lower():
                return False

        return True
