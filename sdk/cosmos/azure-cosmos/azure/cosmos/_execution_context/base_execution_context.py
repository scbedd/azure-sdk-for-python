# The MIT License (MIT)
# Copyright (c) 2014 Microsoft Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Internal class for query execution context implementation in the Azure Cosmos database service.
"""

from collections import deque
from .. import _retry_utility
from .. import http_constants

# pylint: disable=protected-access


class _QueryExecutionContextBase(object):
    """
    This is the abstract base execution context class.
    """

    def __init__(self, client, options):
        """
        Constructor

        :param CosmosClient client:
        :param dict options:
            The request options for the request.

        """
        self._client = client
        self._options = options
        self._is_change_feed = "changeFeed" in options and options["changeFeed"] is True
        self._continuation = None
        if "continuation" in options and self._is_change_feed:
            self._continuation = options["continuation"]
        self._has_started = False
        self._has_finished = False
        self._buffer = deque()

    def _has_more_pages(self):
        return not self._has_started or self._continuation

    def fetch_next_block(self):
        """Returns a block of results with respecting retry policy.

        This method only exists for backward compatibility reasons. (Because QueryIterable
        has exposed fetch_next_block api).

        :return:
            List of results.
        :rtype: list
        """
        if not self._has_more_pages():
            return []

        if self._buffer:
            # if there is anything in the buffer returns that
            res = list(self._buffer)
            self._buffer.clear()
            return res

        # fetches the next block
        return self._fetch_next_block()

    def _fetch_next_block(self):
        raise NotImplementedError

    def __iter__(self):
        """Returns itself as an iterator"""
        return self

    def next(self):
        """Returns the next query result.

        :return:
            The next query result.
        :rtype: dict
        :raises StopIteration: If no more result is left.
        """
        if self._has_finished:
            raise StopIteration

        if not self._buffer:

            results = self.fetch_next_block()
            self._buffer.extend(results)

        if not self._buffer:
            raise StopIteration

        return self._buffer.popleft()

    def __next__(self):
        # supports python 3 iterator
        return self.next()

    def _fetch_items_helper_no_retries(self, fetch_function):
        """Fetches more items and doesn't retry on failure

        :return:
            List of fetched items.
        :rtype: list
        """
        fetched_items = []
        # Continues pages till finds a non empty page or all results are exhausted
        while self._continuation or not self._has_started:
            if not self._has_started:
                self._has_started = True
            self._options["continuation"] = self._continuation
            (fetched_items, response_headers) = fetch_function(self._options)
            continuation_key = http_constants.HttpHeaders.Continuation
            # Use Etag as continuation token for change feed queries.
            if self._is_change_feed:
                continuation_key = http_constants.HttpHeaders.ETag
            # In change feed queries, the continuation token is always populated. The hasNext() test is whether
            # there is any items in the response or not.
            if not self._is_change_feed or fetched_items:
                self._continuation = response_headers.get(continuation_key)
            else:
                self._continuation = None
            if fetched_items:
                break
        return fetched_items

    def _fetch_items_helper_with_retries(self, fetch_function):
        def callback():
            return self._fetch_items_helper_no_retries(fetch_function)

        return _retry_utility.Execute(self._client, self._client._global_endpoint_manager, callback)


class _DefaultQueryExecutionContext(_QueryExecutionContextBase):
    """
    This is the default execution context.
    """

    def __init__(self, client, options, fetch_function):
        """
        Constructor

        :param CosmosClient client:
        :param dict options:
            The request options for the request.
        :param method fetch_function:
            Will be invoked for retrieving each page
            Example of `fetch_function`:
            >>> def result_fn(result):
            >>>     return result['Databases']

        """
        super(_DefaultQueryExecutionContext, self).__init__(client, options)
        self._fetch_function = fetch_function

    def _fetch_next_block(self):
        while super(_DefaultQueryExecutionContext, self)._has_more_pages() and not self._buffer:
            return self._fetch_items_helper_with_retries(self._fetch_function)
