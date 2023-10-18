"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class DestinationDynamodbDynamodb(str, Enum):
    DYNAMODB = 'dynamodb'

class DestinationDynamodbDynamoDBRegion(str, Enum):
    r"""The region of the DynamoDB."""
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
class DestinationDynamodb:
    r"""The values required to configure the destination."""
    access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id') }})
    r"""The access key id to access the DynamoDB. Airbyte requires Read and Write permissions to the DynamoDB."""
    dynamodb_table_name_prefix: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamodb_table_name_prefix') }})
    r"""The prefix to use when naming DynamoDB tables."""
    secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key') }})
    r"""The corresponding secret to the access key id."""
    DESTINATION_TYPE: Final[DestinationDynamodbDynamodb] = dataclasses.field(default=DestinationDynamodbDynamodb.DYNAMODB, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    dynamodb_endpoint: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamodb_endpoint'), 'exclude': lambda f: f is None }})
    r"""This is your DynamoDB endpoint url.(if you are working with AWS DynamoDB, just leave empty)."""
    dynamodb_region: Optional[DestinationDynamodbDynamoDBRegion] = dataclasses.field(default=DestinationDynamodbDynamoDBRegion.UNKNOWN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamodb_region'), 'exclude': lambda f: f is None }})
    r"""The region of the DynamoDB."""
    

