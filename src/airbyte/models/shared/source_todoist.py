"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Todoist(str, Enum):
    TODOIST = 'todoist'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTodoist:
    r"""The values required to configure the source."""
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""Your API Token. See <a href=\\"https://todoist.com/app/settings/integrations/\\">here</a>. The token is case sensitive."""
    SOURCE_TYPE: Final[Todoist] = dataclasses.field(default=Todoist.TODOIST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

