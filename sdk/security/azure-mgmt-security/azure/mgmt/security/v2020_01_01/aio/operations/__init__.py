# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._server_vulnerability_assessment_operations import ServerVulnerabilityAssessmentOperations
from ._assessments_metadata_operations import AssessmentsMetadataOperations
from ._assessments_operations import AssessmentsOperations
from ._adaptive_application_controls_operations import AdaptiveApplicationControlsOperations
from ._adaptive_network_hardenings_operations import AdaptiveNetworkHardeningsOperations
from ._allowed_connections_operations import AllowedConnectionsOperations
from ._topology_operations import TopologyOperations
from ._jit_network_access_policies_operations import JitNetworkAccessPoliciesOperations
from ._discovered_security_solutions_operations import DiscoveredSecuritySolutionsOperations
from ._security_solutions_reference_data_operations import SecuritySolutionsReferenceDataOperations
from ._external_security_solutions_operations import ExternalSecuritySolutionsOperations
from ._secure_scores_operations import SecureScoresOperations
from ._secure_score_controls_operations import SecureScoreControlsOperations
from ._secure_score_control_definitions_operations import SecureScoreControlDefinitionsOperations
from ._security_solutions_operations import SecuritySolutionsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ServerVulnerabilityAssessmentOperations",
    "AssessmentsMetadataOperations",
    "AssessmentsOperations",
    "AdaptiveApplicationControlsOperations",
    "AdaptiveNetworkHardeningsOperations",
    "AllowedConnectionsOperations",
    "TopologyOperations",
    "JitNetworkAccessPoliciesOperations",
    "DiscoveredSecuritySolutionsOperations",
    "SecuritySolutionsReferenceDataOperations",
    "ExternalSecuritySolutionsOperations",
    "SecureScoresOperations",
    "SecureScoreControlsOperations",
    "SecureScoreControlDefinitionsOperations",
    "SecuritySolutionsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
