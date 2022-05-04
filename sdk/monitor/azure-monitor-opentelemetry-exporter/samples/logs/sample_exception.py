# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
An example showing how to export exception telemetry using the AzureMonitorLogExporter.
"""
import os
import logging

from opentelemetry.sdk._logs import (
    LogEmitterProvider,
    OTLPHandler,
    get_log_emitter_provider,
    set_log_emitter_provider,
)
from opentelemetry.sdk._logs.export import BatchLogProcessor

from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter

set_log_emitter_provider(LogEmitterProvider())
exporter = AzureMonitorLogExporter.from_connection_string(
    os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"]
)
get_log_emitter_provider().add_log_processor(BatchLogProcessor(exporter))

# Attach OTel handler to namespaced logger
handler = OTLPHandler()
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.exception("Error: Division by zero")
