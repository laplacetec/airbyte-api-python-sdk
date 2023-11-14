"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Coda(str, Enum):
    CODA = 'coda'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCoda:
    r"""The values required to configure the source."""
    auth_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_token') }})
    r"""Bearer token"""
    SOURCE_TYPE: Final[Coda] = dataclasses.field(default=Coda.CODA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

