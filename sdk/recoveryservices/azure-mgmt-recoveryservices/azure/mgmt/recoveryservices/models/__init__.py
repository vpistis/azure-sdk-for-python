# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureMonitorAlertSettings
from ._models_py3 import CertificateRequest
from ._models_py3 import CheckNameAvailabilityParameters
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import ClassicAlertSettings
from ._models_py3 import ClientDiscoveryDisplay
from ._models_py3 import ClientDiscoveryForLogSpecification
from ._models_py3 import ClientDiscoveryForProperties
from ._models_py3 import ClientDiscoveryForServiceSpecification
from ._models_py3 import ClientDiscoveryResponse
from ._models_py3 import ClientDiscoveryValueForSingleApi
from ._models_py3 import CmkKekIdentity
from ._models_py3 import CmkKeyVaultProperties
from ._models_py3 import Error
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import IdentityData
from ._models_py3 import JobsSummary
from ._models_py3 import MonitoringSettings
from ._models_py3 import MonitoringSummary
from ._models_py3 import NameInfo
from ._models_py3 import OperationResource
from ._models_py3 import PatchTrackedResource
from ._models_py3 import PatchVault
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionVaultProperties
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResources
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import RawCertificateData
from ._models_py3 import ReplicationUsage
from ._models_py3 import ReplicationUsageList
from ._models_py3 import Resource
from ._models_py3 import ResourceCertificateAndAadDetails
from ._models_py3 import ResourceCertificateAndAcsDetails
from ._models_py3 import ResourceCertificateDetails
from ._models_py3 import Sku
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UpgradeDetails
from ._models_py3 import UserIdentity
from ._models_py3 import Vault
from ._models_py3 import VaultCertificateResponse
from ._models_py3 import VaultExtendedInfoResource
from ._models_py3 import VaultList
from ._models_py3 import VaultProperties
from ._models_py3 import VaultPropertiesEncryption
from ._models_py3 import VaultPropertiesMoveDetails
from ._models_py3 import VaultPropertiesRedundancySettings
from ._models_py3 import VaultUsage
from ._models_py3 import VaultUsageList


from ._recovery_services_client_enums import (
    AlertsState,
    AuthType,
    BackupStorageVersion,
    CreatedByType,
    CrossRegionRestore,
    InfrastructureEncryptionState,
    PrivateEndpointConnectionStatus,
    ProvisioningState,
    ResourceIdentityType,
    ResourceMoveState,
    SkuName,
    StandardTierStorageRedundancy,
    TriggerType,
    UsagesUnit,
    VaultPrivateEndpointState,
    VaultUpgradeState,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AzureMonitorAlertSettings',
    'CertificateRequest',
    'CheckNameAvailabilityParameters',
    'CheckNameAvailabilityResult',
    'ClassicAlertSettings',
    'ClientDiscoveryDisplay',
    'ClientDiscoveryForLogSpecification',
    'ClientDiscoveryForProperties',
    'ClientDiscoveryForServiceSpecification',
    'ClientDiscoveryResponse',
    'ClientDiscoveryValueForSingleApi',
    'CmkKekIdentity',
    'CmkKeyVaultProperties',
    'Error',
    'ErrorAdditionalInfo',
    'IdentityData',
    'JobsSummary',
    'MonitoringSettings',
    'MonitoringSummary',
    'NameInfo',
    'OperationResource',
    'PatchTrackedResource',
    'PatchVault',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionVaultProperties',
    'PrivateLinkResource',
    'PrivateLinkResources',
    'PrivateLinkServiceConnectionState',
    'RawCertificateData',
    'ReplicationUsage',
    'ReplicationUsageList',
    'Resource',
    'ResourceCertificateAndAadDetails',
    'ResourceCertificateAndAcsDetails',
    'ResourceCertificateDetails',
    'Sku',
    'SystemData',
    'TrackedResource',
    'UpgradeDetails',
    'UserIdentity',
    'Vault',
    'VaultCertificateResponse',
    'VaultExtendedInfoResource',
    'VaultList',
    'VaultProperties',
    'VaultPropertiesEncryption',
    'VaultPropertiesMoveDetails',
    'VaultPropertiesRedundancySettings',
    'VaultUsage',
    'VaultUsageList',
    'AlertsState',
    'AuthType',
    'BackupStorageVersion',
    'CreatedByType',
    'CrossRegionRestore',
    'InfrastructureEncryptionState',
    'PrivateEndpointConnectionStatus',
    'ProvisioningState',
    'ResourceIdentityType',
    'ResourceMoveState',
    'SkuName',
    'StandardTierStorageRedundancy',
    'TriggerType',
    'UsagesUnit',
    'VaultPrivateEndpointState',
    'VaultUpgradeState',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()