"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class Dixa(str, Enum):
    DIXA = 'dixa'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDixa:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Dixa API token"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The connector pulls records updated from this date onwards."""
    batch_size: Optional[int] = dataclasses.field(default=31, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    r"""Number of days to batch into one request. Max 31."""
    SOURCE_TYPE: Final[Dixa] = dataclasses.field(default=Dixa.DIXA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

