"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceSquareCredentialsAPIKeyCredentialsTitleEnum(str, Enum):
    API_KEY = 'API Key'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquareCredentialsAPIKey:
    r"""Choose how to authenticate to Square."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The API key for a Square application"""
    credentials_title: Optional[SourceSquareCredentialsAPIKeyCredentialsTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title'), 'exclude': lambda f: f is None }})
    
class SourceSquareCredentialsOauthAuthenticationCredentialsTitleEnum(str, Enum):
    O_AUTH_CREDENTIALS = 'OAuth Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquareCredentialsOauthAuthentication:
    r"""Choose how to authenticate to Square."""
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Square-issued ID of your application"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Square-issued application secret for your application"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""A refresh token generated using the above client ID and secret"""
    credentials_title: Optional[SourceSquareCredentialsOauthAuthenticationCredentialsTitleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title'), 'exclude': lambda f: f is None }})
    
class SourceSquareSquareEnum(str, Enum):
    SQUARE = 'square'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquare:
    r"""The values required to configure the source."""
    
    is_sandbox: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox') }})
    r"""Determines whether to use the sandbox or production environment."""
    source_type: SourceSquareSquareEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Square."""
    include_deleted_objects: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_deleted_objects'), 'exclude': lambda f: f is None }})
    r"""In some streams there is an option to include deleted objects (Items, Categories, Discounts, Taxes)"""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated. If not set, all data will be replicated."""
    