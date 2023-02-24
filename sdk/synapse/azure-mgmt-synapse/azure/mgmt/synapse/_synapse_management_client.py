# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from ._configuration import SynapseManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AzureADOnlyAuthenticationsOperations,
    BigDataPoolsOperations,
    DataMaskingPoliciesOperations,
    DataMaskingRulesOperations,
    ExtendedSqlPoolBlobAuditingPoliciesOperations,
    GetOperations,
    IntegrationRuntimeAuthKeysOperations,
    IntegrationRuntimeConnectionInfosOperations,
    IntegrationRuntimeCredentialsOperations,
    IntegrationRuntimeMonitoringDataOperations,
    IntegrationRuntimeNodeIpAddressOperations,
    IntegrationRuntimeNodesOperations,
    IntegrationRuntimeObjectMetadataOperations,
    IntegrationRuntimeStatusOperations,
    IntegrationRuntimesOperations,
    IpFirewallRulesOperations,
    KeysOperations,
    KustoOperationsOperations,
    KustoPoolAttachedDatabaseConfigurationsOperations,
    KustoPoolChildResourceOperations,
    KustoPoolDataConnectionsOperations,
    KustoPoolDatabasePrincipalAssignmentsOperations,
    KustoPoolDatabasesOperations,
    KustoPoolPrincipalAssignmentsOperations,
    KustoPoolPrivateLinkResourcesOperations,
    KustoPoolsOperations,
    LibrariesOperations,
    LibraryOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateEndpointConnectionsPrivateLinkHubOperations,
    PrivateLinkHubPrivateLinkResourcesOperations,
    PrivateLinkHubsOperations,
    PrivateLinkResourcesOperations,
    RestorableDroppedSqlPoolsOperations,
    SparkConfigurationOperations,
    SparkConfigurationsOperations,
    SqlPoolBlobAuditingPoliciesOperations,
    SqlPoolColumnsOperations,
    SqlPoolConnectionPoliciesOperations,
    SqlPoolDataWarehouseUserActivitiesOperations,
    SqlPoolGeoBackupPoliciesOperations,
    SqlPoolMaintenanceWindowOptionsOperations,
    SqlPoolMaintenanceWindowsOperations,
    SqlPoolMetadataSyncConfigsOperations,
    SqlPoolOperationResultsOperations,
    SqlPoolOperationsOperations,
    SqlPoolRecommendedSensitivityLabelsOperations,
    SqlPoolReplicationLinksOperations,
    SqlPoolRestorePointsOperations,
    SqlPoolSchemasOperations,
    SqlPoolSecurityAlertPoliciesOperations,
    SqlPoolSensitivityLabelsOperations,
    SqlPoolTableColumnsOperations,
    SqlPoolTablesOperations,
    SqlPoolTransparentDataEncryptionsOperations,
    SqlPoolUsagesOperations,
    SqlPoolVulnerabilityAssessmentRuleBaselinesOperations,
    SqlPoolVulnerabilityAssessmentScansOperations,
    SqlPoolVulnerabilityAssessmentsOperations,
    SqlPoolWorkloadClassifierOperations,
    SqlPoolWorkloadGroupOperations,
    SqlPoolsOperations,
    WorkspaceAadAdminsOperations,
    WorkspaceManagedIdentitySqlControlSettingsOperations,
    WorkspaceManagedSqlServerBlobAuditingPoliciesOperations,
    WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettingsOperations,
    WorkspaceManagedSqlServerEncryptionProtectorOperations,
    WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations,
    WorkspaceManagedSqlServerRecoverableSqlPoolsOperations,
    WorkspaceManagedSqlServerSecurityAlertPolicyOperations,
    WorkspaceManagedSqlServerUsagesOperations,
    WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations,
    WorkspaceSqlAadAdminsOperations,
    WorkspacesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class SynapseManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Azure Synapse Analytics Management Client.

    :ivar azure_ad_only_authentications: AzureADOnlyAuthenticationsOperations operations
    :vartype azure_ad_only_authentications:
     azure.mgmt.synapse.operations.AzureADOnlyAuthenticationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.synapse.operations.Operations
    :ivar ip_firewall_rules: IpFirewallRulesOperations operations
    :vartype ip_firewall_rules: azure.mgmt.synapse.operations.IpFirewallRulesOperations
    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.synapse.operations.KeysOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.synapse.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.synapse.operations.PrivateLinkResourcesOperations
    :ivar private_link_hub_private_link_resources: PrivateLinkHubPrivateLinkResourcesOperations
     operations
    :vartype private_link_hub_private_link_resources:
     azure.mgmt.synapse.operations.PrivateLinkHubPrivateLinkResourcesOperations
    :ivar private_link_hubs: PrivateLinkHubsOperations operations
    :vartype private_link_hubs: azure.mgmt.synapse.operations.PrivateLinkHubsOperations
    :ivar private_endpoint_connections_private_link_hub:
     PrivateEndpointConnectionsPrivateLinkHubOperations operations
    :vartype private_endpoint_connections_private_link_hub:
     azure.mgmt.synapse.operations.PrivateEndpointConnectionsPrivateLinkHubOperations
    :ivar sql_pools: SqlPoolsOperations operations
    :vartype sql_pools: azure.mgmt.synapse.operations.SqlPoolsOperations
    :ivar sql_pool_metadata_sync_configs: SqlPoolMetadataSyncConfigsOperations operations
    :vartype sql_pool_metadata_sync_configs:
     azure.mgmt.synapse.operations.SqlPoolMetadataSyncConfigsOperations
    :ivar sql_pool_operation_results: SqlPoolOperationResultsOperations operations
    :vartype sql_pool_operation_results:
     azure.mgmt.synapse.operations.SqlPoolOperationResultsOperations
    :ivar sql_pool_geo_backup_policies: SqlPoolGeoBackupPoliciesOperations operations
    :vartype sql_pool_geo_backup_policies:
     azure.mgmt.synapse.operations.SqlPoolGeoBackupPoliciesOperations
    :ivar sql_pool_data_warehouse_user_activities: SqlPoolDataWarehouseUserActivitiesOperations
     operations
    :vartype sql_pool_data_warehouse_user_activities:
     azure.mgmt.synapse.operations.SqlPoolDataWarehouseUserActivitiesOperations
    :ivar sql_pool_restore_points: SqlPoolRestorePointsOperations operations
    :vartype sql_pool_restore_points: azure.mgmt.synapse.operations.SqlPoolRestorePointsOperations
    :ivar sql_pool_replication_links: SqlPoolReplicationLinksOperations operations
    :vartype sql_pool_replication_links:
     azure.mgmt.synapse.operations.SqlPoolReplicationLinksOperations
    :ivar sql_pool_maintenance_windows: SqlPoolMaintenanceWindowsOperations operations
    :vartype sql_pool_maintenance_windows:
     azure.mgmt.synapse.operations.SqlPoolMaintenanceWindowsOperations
    :ivar sql_pool_maintenance_window_options: SqlPoolMaintenanceWindowOptionsOperations operations
    :vartype sql_pool_maintenance_window_options:
     azure.mgmt.synapse.operations.SqlPoolMaintenanceWindowOptionsOperations
    :ivar sql_pool_transparent_data_encryptions: SqlPoolTransparentDataEncryptionsOperations
     operations
    :vartype sql_pool_transparent_data_encryptions:
     azure.mgmt.synapse.operations.SqlPoolTransparentDataEncryptionsOperations
    :ivar sql_pool_blob_auditing_policies: SqlPoolBlobAuditingPoliciesOperations operations
    :vartype sql_pool_blob_auditing_policies:
     azure.mgmt.synapse.operations.SqlPoolBlobAuditingPoliciesOperations
    :ivar sql_pool_operations: SqlPoolOperationsOperations operations
    :vartype sql_pool_operations: azure.mgmt.synapse.operations.SqlPoolOperationsOperations
    :ivar sql_pool_usages: SqlPoolUsagesOperations operations
    :vartype sql_pool_usages: azure.mgmt.synapse.operations.SqlPoolUsagesOperations
    :ivar sql_pool_sensitivity_labels: SqlPoolSensitivityLabelsOperations operations
    :vartype sql_pool_sensitivity_labels:
     azure.mgmt.synapse.operations.SqlPoolSensitivityLabelsOperations
    :ivar sql_pool_recommended_sensitivity_labels: SqlPoolRecommendedSensitivityLabelsOperations
     operations
    :vartype sql_pool_recommended_sensitivity_labels:
     azure.mgmt.synapse.operations.SqlPoolRecommendedSensitivityLabelsOperations
    :ivar sql_pool_schemas: SqlPoolSchemasOperations operations
    :vartype sql_pool_schemas: azure.mgmt.synapse.operations.SqlPoolSchemasOperations
    :ivar sql_pool_tables: SqlPoolTablesOperations operations
    :vartype sql_pool_tables: azure.mgmt.synapse.operations.SqlPoolTablesOperations
    :ivar sql_pool_table_columns: SqlPoolTableColumnsOperations operations
    :vartype sql_pool_table_columns: azure.mgmt.synapse.operations.SqlPoolTableColumnsOperations
    :ivar sql_pool_connection_policies: SqlPoolConnectionPoliciesOperations operations
    :vartype sql_pool_connection_policies:
     azure.mgmt.synapse.operations.SqlPoolConnectionPoliciesOperations
    :ivar sql_pool_vulnerability_assessments: SqlPoolVulnerabilityAssessmentsOperations operations
    :vartype sql_pool_vulnerability_assessments:
     azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentsOperations
    :ivar sql_pool_vulnerability_assessment_scans: SqlPoolVulnerabilityAssessmentScansOperations
     operations
    :vartype sql_pool_vulnerability_assessment_scans:
     azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentScansOperations
    :ivar sql_pool_security_alert_policies: SqlPoolSecurityAlertPoliciesOperations operations
    :vartype sql_pool_security_alert_policies:
     azure.mgmt.synapse.operations.SqlPoolSecurityAlertPoliciesOperations
    :ivar sql_pool_vulnerability_assessment_rule_baselines:
     SqlPoolVulnerabilityAssessmentRuleBaselinesOperations operations
    :vartype sql_pool_vulnerability_assessment_rule_baselines:
     azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
    :ivar extended_sql_pool_blob_auditing_policies: ExtendedSqlPoolBlobAuditingPoliciesOperations
     operations
    :vartype extended_sql_pool_blob_auditing_policies:
     azure.mgmt.synapse.operations.ExtendedSqlPoolBlobAuditingPoliciesOperations
    :ivar data_masking_policies: DataMaskingPoliciesOperations operations
    :vartype data_masking_policies: azure.mgmt.synapse.operations.DataMaskingPoliciesOperations
    :ivar data_masking_rules: DataMaskingRulesOperations operations
    :vartype data_masking_rules: azure.mgmt.synapse.operations.DataMaskingRulesOperations
    :ivar sql_pool_columns: SqlPoolColumnsOperations operations
    :vartype sql_pool_columns: azure.mgmt.synapse.operations.SqlPoolColumnsOperations
    :ivar sql_pool_workload_group: SqlPoolWorkloadGroupOperations operations
    :vartype sql_pool_workload_group: azure.mgmt.synapse.operations.SqlPoolWorkloadGroupOperations
    :ivar sql_pool_workload_classifier: SqlPoolWorkloadClassifierOperations operations
    :vartype sql_pool_workload_classifier:
     azure.mgmt.synapse.operations.SqlPoolWorkloadClassifierOperations
    :ivar workspace_managed_sql_server_blob_auditing_policies:
     WorkspaceManagedSqlServerBlobAuditingPoliciesOperations operations
    :vartype workspace_managed_sql_server_blob_auditing_policies:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_extended_blob_auditing_policies:
     WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations operations
    :vartype workspace_managed_sql_server_extended_blob_auditing_policies:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_security_alert_policy:
     WorkspaceManagedSqlServerSecurityAlertPolicyOperations operations
    :vartype workspace_managed_sql_server_security_alert_policy:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerSecurityAlertPolicyOperations
    :ivar workspace_managed_sql_server_vulnerability_assessments:
     WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations operations
    :vartype workspace_managed_sql_server_vulnerability_assessments:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
    :ivar workspace_managed_sql_server_encryption_protector:
     WorkspaceManagedSqlServerEncryptionProtectorOperations operations
    :vartype workspace_managed_sql_server_encryption_protector:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerEncryptionProtectorOperations
    :ivar workspace_managed_sql_server_usages: WorkspaceManagedSqlServerUsagesOperations operations
    :vartype workspace_managed_sql_server_usages:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerUsagesOperations
    :ivar workspace_managed_sql_server_recoverable_sql_pools:
     WorkspaceManagedSqlServerRecoverableSqlPoolsOperations operations
    :vartype workspace_managed_sql_server_recoverable_sql_pools:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerRecoverableSqlPoolsOperations
    :ivar workspace_managed_sql_server_dedicated_sql_minimal_tls_settings:
     WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettingsOperations operations
    :vartype workspace_managed_sql_server_dedicated_sql_minimal_tls_settings:
     azure.mgmt.synapse.operations.WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettingsOperations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.synapse.operations.WorkspacesOperations
    :ivar workspace_aad_admins: WorkspaceAadAdminsOperations operations
    :vartype workspace_aad_admins: azure.mgmt.synapse.operations.WorkspaceAadAdminsOperations
    :ivar workspace_sql_aad_admins: WorkspaceSqlAadAdminsOperations operations
    :vartype workspace_sql_aad_admins:
     azure.mgmt.synapse.operations.WorkspaceSqlAadAdminsOperations
    :ivar workspace_managed_identity_sql_control_settings:
     WorkspaceManagedIdentitySqlControlSettingsOperations operations
    :vartype workspace_managed_identity_sql_control_settings:
     azure.mgmt.synapse.operations.WorkspaceManagedIdentitySqlControlSettingsOperations
    :ivar restorable_dropped_sql_pools: RestorableDroppedSqlPoolsOperations operations
    :vartype restorable_dropped_sql_pools:
     azure.mgmt.synapse.operations.RestorableDroppedSqlPoolsOperations
    :ivar big_data_pools: BigDataPoolsOperations operations
    :vartype big_data_pools: azure.mgmt.synapse.operations.BigDataPoolsOperations
    :ivar library: LibraryOperations operations
    :vartype library: azure.mgmt.synapse.operations.LibraryOperations
    :ivar libraries: LibrariesOperations operations
    :vartype libraries: azure.mgmt.synapse.operations.LibrariesOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.mgmt.synapse.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_node_ip_address: IntegrationRuntimeNodeIpAddressOperations operations
    :vartype integration_runtime_node_ip_address:
     azure.mgmt.synapse.operations.IntegrationRuntimeNodeIpAddressOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations
     operations
    :vartype integration_runtime_object_metadata:
     azure.mgmt.synapse.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodesOperations operations
    :vartype integration_runtime_nodes:
     azure.mgmt.synapse.operations.IntegrationRuntimeNodesOperations
    :ivar integration_runtime_credentials: IntegrationRuntimeCredentialsOperations operations
    :vartype integration_runtime_credentials:
     azure.mgmt.synapse.operations.IntegrationRuntimeCredentialsOperations
    :ivar integration_runtime_connection_infos: IntegrationRuntimeConnectionInfosOperations
     operations
    :vartype integration_runtime_connection_infos:
     azure.mgmt.synapse.operations.IntegrationRuntimeConnectionInfosOperations
    :ivar integration_runtime_auth_keys: IntegrationRuntimeAuthKeysOperations operations
    :vartype integration_runtime_auth_keys:
     azure.mgmt.synapse.operations.IntegrationRuntimeAuthKeysOperations
    :ivar integration_runtime_monitoring_data: IntegrationRuntimeMonitoringDataOperations
     operations
    :vartype integration_runtime_monitoring_data:
     azure.mgmt.synapse.operations.IntegrationRuntimeMonitoringDataOperations
    :ivar integration_runtime_status: IntegrationRuntimeStatusOperations operations
    :vartype integration_runtime_status:
     azure.mgmt.synapse.operations.IntegrationRuntimeStatusOperations
    :ivar get: GetOperations operations
    :vartype get: azure.mgmt.synapse.operations.GetOperations
    :ivar spark_configuration: SparkConfigurationOperations operations
    :vartype spark_configuration: azure.mgmt.synapse.operations.SparkConfigurationOperations
    :ivar spark_configurations: SparkConfigurationsOperations operations
    :vartype spark_configurations: azure.mgmt.synapse.operations.SparkConfigurationsOperations
    :ivar kusto_operations: KustoOperationsOperations operations
    :vartype kusto_operations: azure.mgmt.synapse.operations.KustoOperationsOperations
    :ivar kusto_pools: KustoPoolsOperations operations
    :vartype kusto_pools: azure.mgmt.synapse.operations.KustoPoolsOperations
    :ivar kusto_pool_child_resource: KustoPoolChildResourceOperations operations
    :vartype kusto_pool_child_resource:
     azure.mgmt.synapse.operations.KustoPoolChildResourceOperations
    :ivar kusto_pool_attached_database_configurations:
     KustoPoolAttachedDatabaseConfigurationsOperations operations
    :vartype kusto_pool_attached_database_configurations:
     azure.mgmt.synapse.operations.KustoPoolAttachedDatabaseConfigurationsOperations
    :ivar kusto_pool_databases: KustoPoolDatabasesOperations operations
    :vartype kusto_pool_databases: azure.mgmt.synapse.operations.KustoPoolDatabasesOperations
    :ivar kusto_pool_data_connections: KustoPoolDataConnectionsOperations operations
    :vartype kusto_pool_data_connections:
     azure.mgmt.synapse.operations.KustoPoolDataConnectionsOperations
    :ivar kusto_pool_principal_assignments: KustoPoolPrincipalAssignmentsOperations operations
    :vartype kusto_pool_principal_assignments:
     azure.mgmt.synapse.operations.KustoPoolPrincipalAssignmentsOperations
    :ivar kusto_pool_database_principal_assignments:
     KustoPoolDatabasePrincipalAssignmentsOperations operations
    :vartype kusto_pool_database_principal_assignments:
     azure.mgmt.synapse.operations.KustoPoolDatabasePrincipalAssignmentsOperations
    :ivar kusto_pool_private_link_resources: KustoPoolPrivateLinkResourcesOperations operations
    :vartype kusto_pool_private_link_resources:
     azure.mgmt.synapse.operations.KustoPoolPrivateLinkResourcesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = SynapseManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.azure_ad_only_authentications = AzureADOnlyAuthenticationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.ip_firewall_rules = IpFirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.keys = KeysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_hub_private_link_resources = PrivateLinkHubPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_hubs = PrivateLinkHubsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections_private_link_hub = PrivateEndpointConnectionsPrivateLinkHubOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pools = SqlPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_metadata_sync_configs = SqlPoolMetadataSyncConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_operation_results = SqlPoolOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_geo_backup_policies = SqlPoolGeoBackupPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_data_warehouse_user_activities = SqlPoolDataWarehouseUserActivitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_restore_points = SqlPoolRestorePointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_replication_links = SqlPoolReplicationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_maintenance_windows = SqlPoolMaintenanceWindowsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_maintenance_window_options = SqlPoolMaintenanceWindowOptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_transparent_data_encryptions = SqlPoolTransparentDataEncryptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_blob_auditing_policies = SqlPoolBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_operations = SqlPoolOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_usages = SqlPoolUsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_sensitivity_labels = SqlPoolSensitivityLabelsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_recommended_sensitivity_labels = SqlPoolRecommendedSensitivityLabelsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_schemas = SqlPoolSchemasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_tables = SqlPoolTablesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_table_columns = SqlPoolTableColumnsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_connection_policies = SqlPoolConnectionPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_vulnerability_assessments = SqlPoolVulnerabilityAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_vulnerability_assessment_scans = SqlPoolVulnerabilityAssessmentScansOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_security_alert_policies = SqlPoolSecurityAlertPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_vulnerability_assessment_rule_baselines = SqlPoolVulnerabilityAssessmentRuleBaselinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extended_sql_pool_blob_auditing_policies = ExtendedSqlPoolBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_masking_policies = DataMaskingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_masking_rules = DataMaskingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_columns = SqlPoolColumnsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_workload_group = SqlPoolWorkloadGroupOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pool_workload_classifier = SqlPoolWorkloadClassifierOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_managed_sql_server_blob_auditing_policies = (
            WorkspaceManagedSqlServerBlobAuditingPoliciesOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.workspace_managed_sql_server_extended_blob_auditing_policies = (
            WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.workspace_managed_sql_server_security_alert_policy = (
            WorkspaceManagedSqlServerSecurityAlertPolicyOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.workspace_managed_sql_server_vulnerability_assessments = (
            WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.workspace_managed_sql_server_encryption_protector = WorkspaceManagedSqlServerEncryptionProtectorOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_managed_sql_server_usages = WorkspaceManagedSqlServerUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_managed_sql_server_recoverable_sql_pools = (
            WorkspaceManagedSqlServerRecoverableSqlPoolsOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.workspace_managed_sql_server_dedicated_sql_minimal_tls_settings = (
            WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettingsOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.workspaces = WorkspacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_aad_admins = WorkspaceAadAdminsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_sql_aad_admins = WorkspaceSqlAadAdminsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_managed_identity_sql_control_settings = WorkspaceManagedIdentitySqlControlSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_dropped_sql_pools = RestorableDroppedSqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.big_data_pools = BigDataPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.library = LibraryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.libraries = LibrariesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_node_ip_address = IntegrationRuntimeNodeIpAddressOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_credentials = IntegrationRuntimeCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_connection_infos = IntegrationRuntimeConnectionInfosOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_auth_keys = IntegrationRuntimeAuthKeysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_monitoring_data = IntegrationRuntimeMonitoringDataOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_status = IntegrationRuntimeStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.get = GetOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spark_configuration = SparkConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spark_configurations = SparkConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_operations = KustoOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pools = KustoPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_child_resource = KustoPoolChildResourceOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pool_attached_database_configurations = KustoPoolAttachedDatabaseConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pool_databases = KustoPoolDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pool_data_connections = KustoPoolDataConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pool_principal_assignments = KustoPoolPrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pool_database_principal_assignments = KustoPoolDatabasePrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.kusto_pool_private_link_resources = KustoPoolPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "SynapseManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
