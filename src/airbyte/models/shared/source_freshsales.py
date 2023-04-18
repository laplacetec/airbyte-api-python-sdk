"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceFreshsalesFreshsalesEnum(str, Enum):
    FRESHSALES = 'freshsales'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFreshsales:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Freshsales API Key. See <a href=\\"https://crmsupport.freshworks.com/support/solutions/articles/50000002503-how-to-find-my-api-key-\\">here</a>. The key is case sensitive."""  
    domain_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_name') }})
    r"""The Name of your Freshsales domain"""  
    source_type: SourceFreshsalesFreshsalesEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    