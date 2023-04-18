"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields

class SourceKlaviyoKlaviyoEnum(str, Enum):
    KLAVIYO = 'klaviyo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceKlaviyo:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Klaviyo API Key. See our <a href=\\"https://docs.airbyte.com/integrations/sources/klaviyo\\">docs</a> if you need help finding this key."""  
    source_type: SourceKlaviyoKlaviyoEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""  
    