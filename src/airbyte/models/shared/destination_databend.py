"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationDatabendDatabendEnum(str, Enum):
    DATABEND = 'databend'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabend:
    r"""The values required to configure the destination."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""  
    destination_type: DestinationDatabendDatabendEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})  
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""  
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""  
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""  
    port: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the database."""  
    table: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table'), 'exclude': lambda f: f is None }})
    r"""The default  table was written to."""  
    