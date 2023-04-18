"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourcePokeapiPokeapiEnum(str, Enum):
    POKEAPI = 'pokeapi'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePokeapi:
    r"""The values required to configure the source."""
    
    pokemon_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pokemon_name') }})
    r"""Pokemon requested from the API."""  
    source_type: SourcePokeapiPokeapiEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    