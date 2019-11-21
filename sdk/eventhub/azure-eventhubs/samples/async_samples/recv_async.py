#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
An example to show receiving events from an Event Hub asynchronously.
"""

import asyncio
import os
from azure.eventhub.aio import EventHubConsumerClient

CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]
EVENTHUB_NAME = os.environ['EVENT_HUB_NAME']


async def on_event(partition_context, event):
    print("Received event from partition: {}".format(partition_context.partition_id))
    # Do some sync or async operations. If the operation is i/o intensive, async will have better performance
    # print(event)


async def receive(client):
    try:
        await client.receive(on_event=on_event, consumer_group="$default")
    except KeyboardInterrupt:
        await client.close()


async def main():
    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        eventhub_name=EVENTHUB_NAME
    )
    async with client:
        await receive(client)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
