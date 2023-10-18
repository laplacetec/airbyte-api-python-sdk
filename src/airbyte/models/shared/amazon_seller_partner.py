"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AmazonSellerPartner:
    r"""The values required to configure the source."""
    lwa_app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lwa_app_id'), 'exclude': lambda f: f is None }})
    r"""Your Login with Amazon Client ID."""
    lwa_client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lwa_client_secret'), 'exclude': lambda f: f is None }})
    r"""Your Login with Amazon Client Secret."""
    

