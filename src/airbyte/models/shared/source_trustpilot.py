"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceTrustpilotCredentialsAPIKeyAuthTypeEnum(str, Enum):
    APIKEY = 'apikey'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTrustpilotCredentialsAPIKey:
    r"""The API key authentication method gives you access to only the streams which are part of the Public API. When you want to get streams available via the Consumer API (e.g. the private reviews) you need to use authentication method OAuth 2.0."""
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The API key of the Trustpilot API application."""  
    auth_type: Optional[SourceTrustpilotCredentialsAPIKeyAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})  
    
class SourceTrustpilotCredentialsOAuth20AuthTypeEnum(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTrustpilotCredentialsOAuth20:
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""  
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The API key of the Trustpilot API application. (represents the OAuth Client ID)"""  
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Secret of the Trustpilot API application. (represents the OAuth Client Secret)"""  
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access_token."""  
    token_expiry_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date-time when the access token should be refreshed."""  
    auth_type: Optional[SourceTrustpilotCredentialsOAuth20AuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})  
    
class SourceTrustpilotTrustpilotEnum(str, Enum):
    TRUSTPILOT = 'trustpilot'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTrustpilot:
    r"""The values required to configure the source."""
    
    business_units: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('business_units') }})
    r"""The names of business units which shall be synchronized. Some streams e.g. configured_business_units or private_reviews use this configuration."""  
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})  
    source_type: SourceTrustpilotTrustpilotEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""For streams with sync. method incremental the start date time to be used"""  
    