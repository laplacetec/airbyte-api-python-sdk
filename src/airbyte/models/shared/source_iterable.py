"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields

class SourceIterableIterableEnum(str, Enum):
    ITERABLE = 'iterable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceIterable:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Iterable API Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/iterable\\">docs</a> for more information on how to obtain this key."""  
    source_type: SourceIterableIterableEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date from which you'd like to replicate data for Iterable, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""  
    