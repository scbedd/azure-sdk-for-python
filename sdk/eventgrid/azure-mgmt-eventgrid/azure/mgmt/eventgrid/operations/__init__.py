# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._ca_certificates_operations import CaCertificatesOperations
from ._channels_operations import ChannelsOperations
from ._client_groups_operations import ClientGroupsOperations
from ._clients_operations import ClientsOperations
from ._domains_operations import DomainsOperations
from ._domain_topics_operations import DomainTopicsOperations
from ._domain_topic_event_subscriptions_operations import DomainTopicEventSubscriptionsOperations
from ._topic_event_subscriptions_operations import TopicEventSubscriptionsOperations
from ._domain_event_subscriptions_operations import DomainEventSubscriptionsOperations
from ._event_subscriptions_operations import EventSubscriptionsOperations
from ._system_topic_event_subscriptions_operations import SystemTopicEventSubscriptionsOperations
from ._namespace_topic_event_subscriptions_operations import NamespaceTopicEventSubscriptionsOperations
from ._partner_topic_event_subscriptions_operations import PartnerTopicEventSubscriptionsOperations
from ._namespaces_operations import NamespacesOperations
from ._namespace_topics_operations import NamespaceTopicsOperations
from ._operations import Operations
from ._partner_configurations_operations import PartnerConfigurationsOperations
from ._partner_destinations_operations import PartnerDestinationsOperations
from ._partner_namespaces_operations import PartnerNamespacesOperations
from ._partner_registrations_operations import PartnerRegistrationsOperations
from ._partner_topics_operations import PartnerTopicsOperations
from ._permission_bindings_operations import PermissionBindingsOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._system_topics_operations import SystemTopicsOperations
from ._topics_operations import TopicsOperations
from ._extension_topics_operations import ExtensionTopicsOperations
from ._topic_spaces_operations import TopicSpacesOperations
from ._topic_types_operations import TopicTypesOperations
from ._verified_partners_operations import VerifiedPartnersOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CaCertificatesOperations",
    "ChannelsOperations",
    "ClientGroupsOperations",
    "ClientsOperations",
    "DomainsOperations",
    "DomainTopicsOperations",
    "DomainTopicEventSubscriptionsOperations",
    "TopicEventSubscriptionsOperations",
    "DomainEventSubscriptionsOperations",
    "EventSubscriptionsOperations",
    "SystemTopicEventSubscriptionsOperations",
    "NamespaceTopicEventSubscriptionsOperations",
    "PartnerTopicEventSubscriptionsOperations",
    "NamespacesOperations",
    "NamespaceTopicsOperations",
    "Operations",
    "PartnerConfigurationsOperations",
    "PartnerDestinationsOperations",
    "PartnerNamespacesOperations",
    "PartnerRegistrationsOperations",
    "PartnerTopicsOperations",
    "PermissionBindingsOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "SystemTopicsOperations",
    "TopicsOperations",
    "ExtensionTopicsOperations",
    "TopicSpacesOperations",
    "TopicTypesOperations",
    "VerifiedPartnersOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
