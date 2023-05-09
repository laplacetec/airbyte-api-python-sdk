"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationAwsDatalakeCredentialsIAMUserCredentialsTitleEnum(str, Enum):
    r"""Name of the credentials"""
    IAM_USER = 'IAM User'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAwsDatalakeCredentialsIAMUser:
    r"""Choose How to Authenticate to AWS."""
    
    aws_access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id') }})
    r"""AWS User Access Key Id"""
    aws_secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key') }})
    r"""Secret Access Key"""
    credentials_title: DestinationAwsDatalakeCredentialsIAMUserCredentialsTitleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    r"""Name of the credentials"""
    
class DestinationAwsDatalakeCredentialsIAMRoleCredentialsTitleEnum(str, Enum):
    r"""Name of the credentials"""
    IAM_ROLE = 'IAM Role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAwsDatalakeCredentialsIAMRole:
    r"""Choose How to Authenticate to AWS."""
    
    credentials_title: DestinationAwsDatalakeCredentialsIAMRoleCredentialsTitleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    r"""Name of the credentials"""
    role_arn: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role_arn') }})
    r"""Will assume this role to write data to s3"""
    
class DestinationAwsDatalakeAwsDatalakeEnum(str, Enum):
    AWS_DATALAKE = 'aws-datalake'

class DestinationAwsDatalakeFormatParquetColumnarStorageCompressionCodecOptionalEnum(str, Enum):
    r"""The compression algorithm used to compress data."""
    UNCOMPRESSED = 'UNCOMPRESSED'
    SNAPPY = 'SNAPPY'
    GZIP = 'GZIP'
    ZSTD = 'ZSTD'

class DestinationAwsDatalakeFormatParquetColumnarStorageFormatTypeWildcardEnum(str, Enum):
    PARQUET = 'Parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAwsDatalakeFormatParquetColumnarStorage:
    r"""Format of the data output."""
    
    format_type: DestinationAwsDatalakeFormatParquetColumnarStorageFormatTypeWildcardEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression_codec: Optional[DestinationAwsDatalakeFormatParquetColumnarStorageCompressionCodecOptionalEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec'), 'exclude': lambda f: f is None }})
    r"""The compression algorithm used to compress data."""
    
class DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONCompressionCodecOptionalEnum(str, Enum):
    r"""The compression algorithm used to compress data."""
    UNCOMPRESSED = 'UNCOMPRESSED'
    GZIP = 'GZIP'

class DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONFormatTypeWildcardEnum(str, Enum):
    JSONL = 'JSONL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSON:
    r"""Format of the data output."""
    
    format_type: DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONFormatTypeWildcardEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression_codec: Optional[DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONCompressionCodecOptionalEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec'), 'exclude': lambda f: f is None }})
    r"""The compression algorithm used to compress data."""
    
class DestinationAwsDatalakeChooseHowToPartitionDataEnum(str, Enum):
    r"""Partition data by cursor fields when a cursor field is a date"""
    NO_PARTITIONING = 'NO PARTITIONING'
    DATE = 'DATE'
    YEAR = 'YEAR'
    MONTH = 'MONTH'
    DAY = 'DAY'
    YEAR_MONTH = 'YEAR/MONTH'
    YEAR_MONTH_DAY = 'YEAR/MONTH/DAY'

class DestinationAwsDatalakeS3BucketRegionEnum(str, Enum):
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    UNKNOWN = ''
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'
    AF_SOUTH_1 = 'af-south-1'
    AP_EAST_1 = 'ap-east-1'
    AP_SOUTH_1 = 'ap-south-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_NORTHEAST_3 = 'ap-northeast-3'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    CA_CENTRAL_1 = 'ca-central-1'
    CN_NORTH_1 = 'cn-north-1'
    CN_NORTHWEST_1 = 'cn-northwest-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_NORTH_1 = 'eu-north-1'
    EU_SOUTH_1 = 'eu-south-1'
    EU_WEST_1 = 'eu-west-1'
    EU_WEST_2 = 'eu-west-2'
    EU_WEST_3 = 'eu-west-3'
    SA_EAST_1 = 'sa-east-1'
    ME_SOUTH_1 = 'me-south-1'
    US_GOV_EAST_1 = 'us-gov-east-1'
    US_GOV_WEST_1 = 'us-gov-west-1'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAwsDatalake:
    r"""The values required to configure the destination."""
    
    bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket_name') }})
    r"""The name of the S3 bucket. Read more <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html\\">here</a>."""
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Choose How to Authenticate to AWS."""
    destination_type: DestinationAwsDatalakeAwsDatalakeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    lakeformation_database_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lakeformation_database_name') }})
    r"""The default database this destination will use to create tables in per stream. Can be changed per connection by customizing the namespace."""
    region: DestinationAwsDatalakeS3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    aws_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_account_id'), 'exclude': lambda f: f is None }})
    r"""target aws account id"""
    bucket_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket_prefix'), 'exclude': lambda f: f is None }})
    r"""S3 prefix"""
    format: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Format of the data output."""
    glue_catalog_float_as_decimal: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('glue_catalog_float_as_decimal'), 'exclude': lambda f: f is None }})
    r"""Cast float/double as decimal(38,18). This can help achieve higher accuracy and represent numbers correctly as received from the source."""
    lakeformation_database_default_tag_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lakeformation_database_default_tag_key'), 'exclude': lambda f: f is None }})
    r"""Add a default tag key to databases created by this destination"""
    lakeformation_database_default_tag_values: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lakeformation_database_default_tag_values'), 'exclude': lambda f: f is None }})
    r"""Add default values for the `Tag Key` to databases created by this destination. Comma separate for multiple values."""
    lakeformation_governed_tables: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lakeformation_governed_tables'), 'exclude': lambda f: f is None }})
    r"""Whether to create tables as LF governed tables."""
    partitioning: Optional[DestinationAwsDatalakeChooseHowToPartitionDataEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partitioning'), 'exclude': lambda f: f is None }})
    r"""Partition data by cursor fields when a cursor field is a date"""
    