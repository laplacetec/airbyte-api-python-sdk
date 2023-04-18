"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceE2eTestCloudMockCatalogMultiSchemaTypeEnum(str, Enum):
    MULTI_STREAM = 'MULTI_STREAM'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceE2eTestCloudMockCatalogMultiSchema:
    r"""A catalog with multiple data streams, each with a different schema."""
    
    stream_schemas: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schemas') }})
    r"""A Json object specifying multiple data streams and their schemas. Each key in this object is one stream name. Each value is the schema for that stream. The schema should be compatible with <a href=\\"https://json-schema.org/draft-07/json-schema-release-notes.html\\">draft-07</a>. See <a href=\\"https://cswr.github.io/JsonSchema/spec/introduction/\\">this doc</a> for examples."""  
    type: SourceE2eTestCloudMockCatalogMultiSchemaTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    
class SourceE2eTestCloudMockCatalogSingleSchemaTypeEnum(str, Enum):
    SINGLE_STREAM = 'SINGLE_STREAM'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceE2eTestCloudMockCatalogSingleSchema:
    r"""A catalog with one or multiple streams that share the same schema."""
    
    stream_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name') }})
    r"""Name of the data stream."""  
    stream_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schema') }})
    r"""A Json schema for the stream. The schema should be compatible with <a href=\\"https://json-schema.org/draft-07/json-schema-release-notes.html\\">draft-07</a>. See <a href=\\"https://cswr.github.io/JsonSchema/spec/introduction/\\">this doc</a> for examples."""  
    type: SourceE2eTestCloudMockCatalogSingleSchemaTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    stream_duplication: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_duplication'), 'exclude': lambda f: f is None }})
    r"""Duplicate the stream for easy load testing. Each stream name will have a number suffix. For example, if the stream name is \\"ds\\", the duplicated streams will be \\"ds_0\\", \\"ds_1\\", etc."""  
    
class SourceE2eTestCloudE2eTestCloudEnum(str, Enum):
    E2E_TEST_CLOUD = 'e2e-test-cloud'

class SourceE2eTestCloudTypeEnum(str, Enum):
    CONTINUOUS_FEED = 'CONTINUOUS_FEED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceE2eTestCloud:
    r"""The values required to configure the source."""
    
    max_messages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_messages') }})
    r"""Number of records to emit per stream. Min 1. Max 100 billion."""  
    mock_catalog: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mock_catalog') }})  
    source_type: SourceE2eTestCloudE2eTestCloudEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    message_interval_ms: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_interval_ms'), 'exclude': lambda f: f is None }})
    r"""Interval between messages in ms. Min 0 ms. Max 60000 ms (1 minute)."""  
    seed: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    r"""When the seed is unspecified, the current time millis will be used as the seed. Range: [0, 1000000]."""  
    type: Optional[SourceE2eTestCloudTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    