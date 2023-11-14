"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Union

class SourceSalesloftSchemasAuthType(str, Enum):
    API_KEY = 'api_key'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaAPIKey:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key for making authenticated requests. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/salesloft#setup-guide\\">docs</a>"""
    AUTH_TYPE: Final[SourceSalesloftSchemasAuthType] = dataclasses.field(default=SourceSalesloftSchemasAuthType.API_KEY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


class SourceSalesloftAuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaOAuth:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Salesloft developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Salesloft developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining a new access token."""
    token_expiry_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date-time when the access token should be refreshed."""
    AUTH_TYPE: Final[SourceSalesloftAuthType] = dataclasses.field(default=SourceSalesloftAuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


class Salesloft(str, Enum):
    SALESLOFT = 'salesloft'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSalesloft:
    r"""The values required to configure the source."""
    credentials: Union[AuthenticateViaOAuth, AuthenticateViaAPIKey] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for Salesloft API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    SOURCE_TYPE: Final[Salesloft] = dataclasses.field(default=Salesloft.SALESLOFT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

