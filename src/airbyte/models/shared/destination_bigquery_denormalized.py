"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationBigqueryDenormalizedDatasetLocationEnum(str, Enum):
    r"""The location of the dataset. Warning: Changes made after creation will not be applied. The default \\"US\\" value is used if not set explicitly. Read more <a href=\\"https://cloud.google.com/bigquery/docs/locations\\">here</a>."""
    US = 'US'
    EU = 'EU'
    ASIA_EAST1 = 'asia-east1'
    ASIA_EAST2 = 'asia-east2'
    ASIA_NORTHEAST1 = 'asia-northeast1'
    ASIA_NORTHEAST2 = 'asia-northeast2'
    ASIA_NORTHEAST3 = 'asia-northeast3'
    ASIA_SOUTH1 = 'asia-south1'
    ASIA_SOUTH2 = 'asia-south2'
    ASIA_SOUTHEAST1 = 'asia-southeast1'
    ASIA_SOUTHEAST2 = 'asia-southeast2'
    AUSTRALIA_SOUTHEAST1 = 'australia-southeast1'
    AUSTRALIA_SOUTHEAST2 = 'australia-southeast2'
    EUROPE_CENTRAL2 = 'europe-central2'
    EUROPE_NORTH1 = 'europe-north1'
    EUROPE_WEST1 = 'europe-west1'
    EUROPE_WEST2 = 'europe-west2'
    EUROPE_WEST3 = 'europe-west3'
    EUROPE_WEST4 = 'europe-west4'
    EUROPE_WEST6 = 'europe-west6'
    NORTHAMERICA_NORTHEAST1 = 'northamerica-northeast1'
    NORTHAMERICA_NORTHEAST2 = 'northamerica-northeast2'
    SOUTHAMERICA_EAST1 = 'southamerica-east1'
    SOUTHAMERICA_WEST1 = 'southamerica-west1'
    US_CENTRAL1 = 'us-central1'
    US_EAST1 = 'us-east1'
    US_EAST4 = 'us-east4'
    US_WEST1 = 'us-west1'
    US_WEST2 = 'us-west2'
    US_WEST3 = 'us-west3'
    US_WEST4 = 'us-west4'

class DestinationBigqueryDenormalizedBigqueryDenormalizedEnum(str, Enum):
    BIGQUERY_DENORMALIZED = 'bigquery-denormalized'

class DestinationBigqueryDenormalizedLoadingMethodGCSStagingCredentialHMACKeyCredentialTypeEnum(str, Enum):
    HMAC_KEY = 'HMAC_KEY'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryDenormalizedLoadingMethodGCSStagingCredentialHMACKey:
    r"""An HMAC key is a type of credential and can be associated with a service account or a user account in Cloud Storage. Read more <a href=\\"https://cloud.google.com/storage/docs/authentication/hmackeys\\">here</a>."""
    
    credential_type: DestinationBigqueryDenormalizedLoadingMethodGCSStagingCredentialHMACKeyCredentialTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential_type') }})  
    hmac_key_access_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_access_id') }})
    r"""HMAC key access ID. When linked to a service account, this ID is 61 characters long; when linked to a user account, it is 24 characters long."""  
    hmac_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_secret') }})
    r"""The corresponding secret for the access ID. It is a 40-character base-64 encoded string."""  
    
class DestinationBigqueryDenormalizedLoadingMethodGCSStagingGCSTmpFilesAfterwardProcessingEnum(str, Enum):
    r"""This upload method is supposed to temporary store records in GCS bucket. By this select you can chose if these records should be removed from GCS when migration has finished. The default \\"Delete all tmp files from GCS\\" value is used if not set explicitly."""
    DELETE_ALL_TMP_FILES_FROM_GCS = 'Delete all tmp files from GCS'
    KEEP_ALL_TMP_FILES_IN_GCS = 'Keep all tmp files in GCS'

class DestinationBigqueryDenormalizedLoadingMethodGCSStagingMethodEnum(str, Enum):
    GCS_STAGING = 'GCS Staging'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryDenormalizedLoadingMethodGCSStaging:
    r"""Loading method used to send select the way data will be uploaded to BigQuery. <br/><b>Standard Inserts</b> - Direct uploading using SQL INSERT statements. This method is extremely inefficient and provided only for quick testing. In almost all cases, you should use staging. <br/><b>GCS Staging</b> - Writes large batches of records to a file, uploads the file to GCS, then uses <b>COPY INTO table</b> to upload the file. Recommended for most workloads for better speed and scalability. Read more about GCS Staging <a href=\\"https://docs.airbyte.com/integrations/destinations/bigquery#gcs-staging\\">here</a>."""
    
    credential: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential') }})
    r"""An HMAC key is a type of credential and can be associated with a service account or a user account in Cloud Storage. Read more <a href=\\"https://cloud.google.com/storage/docs/authentication/hmackeys\\">here</a>."""  
    gcs_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_name') }})
    r"""The name of the GCS bucket. Read more <a href=\\"https://cloud.google.com/storage/docs/naming-buckets\\">here</a>."""  
    gcs_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_path') }})
    r"""Directory under the GCS bucket where data will be written. Read more <a href=\\"https://cloud.google.com/storage/docs/locations\\">here</a>."""  
    method: DestinationBigqueryDenormalizedLoadingMethodGCSStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})  
    keep_files_in_gcs_bucket: Optional[DestinationBigqueryDenormalizedLoadingMethodGCSStagingGCSTmpFilesAfterwardProcessingEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keep_files_in_gcs-bucket'), 'exclude': lambda f: f is None }})
    r"""This upload method is supposed to temporary store records in GCS bucket. By this select you can chose if these records should be removed from GCS when migration has finished. The default \\"Delete all tmp files from GCS\\" value is used if not set explicitly."""  
    
class DestinationBigqueryDenormalizedLoadingMethodStandardInsertsMethodEnum(str, Enum):
    STANDARD = 'Standard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryDenormalizedLoadingMethodStandardInserts:
    r"""Loading method used to send select the way data will be uploaded to BigQuery. <br/><b>Standard Inserts</b> - Direct uploading using SQL INSERT statements. This method is extremely inefficient and provided only for quick testing. In almost all cases, you should use staging. <br/><b>GCS Staging</b> - Writes large batches of records to a file, uploads the file to GCS, then uses <b>COPY INTO table</b> to upload the file. Recommended for most workloads for better speed and scalability. Read more about GCS Staging <a href=\\"https://docs.airbyte.com/integrations/destinations/bigquery#gcs-staging\\">here</a>."""
    
    method: DestinationBigqueryDenormalizedLoadingMethodStandardInsertsMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryDenormalized:
    r"""The values required to configure the destination."""
    
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id') }})
    r"""The default BigQuery Dataset ID that tables are replicated to if the source does not specify a namespace. Read more <a href=\\"https://cloud.google.com/bigquery/docs/datasets#create-dataset\\">here</a>."""  
    destination_type: DestinationBigqueryDenormalizedBigqueryDenormalizedEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})  
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""The GCP project ID for the project containing the target BigQuery dataset. Read more <a href=\\"https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects\\">here</a>."""  
    big_query_client_buffer_size_mb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('big_query_client_buffer_size_mb'), 'exclude': lambda f: f is None }})
    r"""Google BigQuery client's chunk (buffer) size (MIN=1, MAX = 15) for each table. The size that will be written by a single RPC. Written data will be buffered and only flushed upon reaching this size or closing the channel. The default 15MB value is used if not set explicitly. Read more <a href=\\"https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html\\">here</a>."""  
    credentials_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json'), 'exclude': lambda f: f is None }})
    r"""The contents of the JSON service account key. Check out the <a href=\\"https://docs.airbyte.com/integrations/destinations/bigquery#service-account-key\\">docs</a> if you need help generating this key. Default credentials will be used if this field is left empty."""  
    dataset_location: Optional[DestinationBigqueryDenormalizedDatasetLocationEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_location'), 'exclude': lambda f: f is None }})
    r"""The location of the dataset. Warning: Changes made after creation will not be applied. The default \\"US\\" value is used if not set explicitly. Read more <a href=\\"https://cloud.google.com/bigquery/docs/locations\\">here</a>."""  
    loading_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loading_method'), 'exclude': lambda f: f is None }})
    r"""Loading method used to send select the way data will be uploaded to BigQuery. <br/><b>Standard Inserts</b> - Direct uploading using SQL INSERT statements. This method is extremely inefficient and provided only for quick testing. In almost all cases, you should use staging. <br/><b>GCS Staging</b> - Writes large batches of records to a file, uploads the file to GCS, then uses <b>COPY INTO table</b> to upload the file. Recommended for most workloads for better speed and scalability. Read more about GCS Staging <a href=\\"https://docs.airbyte.com/integrations/destinations/bigquery#gcs-staging\\">here</a>."""  
    