"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class DestinationKinesisKinesis(str, Enum):
    KINESIS = 'kinesis'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationKinesis:
    r"""The values required to configure the destination."""
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessKey') }})
    r"""Generate the AWS Access Key for current user."""
    endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    r"""AWS Kinesis endpoint."""
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privateKey') }})
    r"""The AWS Private Key - a string of numbers and letters that are unique for each account, also known as a \\"recovery phrase\\"."""
    region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""AWS region. Your account determines the Regions that are available to you."""
    DESTINATION_TYPE: Final[DestinationKinesisKinesis] = dataclasses.field(default=DestinationKinesisKinesis.KINESIS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    buffer_size: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bufferSize'), 'exclude': lambda f: f is None }})
    r"""Buffer size for storing kinesis records before being batch streamed."""
    shard_count: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shardCount'), 'exclude': lambda f: f is None }})
    r"""Number of shards to which the data should be streamed."""
    

