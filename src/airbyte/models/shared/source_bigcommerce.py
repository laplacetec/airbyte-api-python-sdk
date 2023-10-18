"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class SourceBigcommerceBigcommerce(str, Enum):
    BIGCOMMERCE = 'bigcommerce'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBigcommerce:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""The date you would like to replicate data. Format: YYYY-MM-DD."""
    store_hash: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('store_hash') }})
    r"""The hash code of the store. For https://api.bigcommerce.com/stores/HASH_CODE/v3/, The store's hash code is 'HASH_CODE'."""
    SOURCE_TYPE: Final[SourceBigcommerceBigcommerce] = dataclasses.field(default=SourceBigcommerceBigcommerce.BIGCOMMERCE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

