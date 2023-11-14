"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class FacebookPages(str, Enum):
    FACEBOOK_PAGES = 'facebook-pages'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFacebookPages:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Facebook Page Access Token"""
    page_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_id') }})
    r"""Page ID"""
    SOURCE_TYPE: Final[FacebookPages] = dataclasses.field(default=FacebookPages.FACEBOOK_PAGES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

