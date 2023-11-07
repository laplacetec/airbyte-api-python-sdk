"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Final, Optional, Union

class SourceZendeskTalkSchemasAuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskTalkOAuth20:
    r"""Zendesk service provides two authentication methods. Choose between: `OAuth2.0` or `API token`."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The value of the API token generated. See the <a href=\\"https://docs.airbyte.com/integrations/sources/zendesk-talk\\">docs</a> for more information."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    AUTH_TYPE: Final[Optional[SourceZendeskTalkSchemasAuthType]] = dataclasses.field(default=SourceZendeskTalkSchemasAuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Client ID"""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""Client Secret"""
    


class SourceZendeskTalkAuthType(str, Enum):
    API_TOKEN = 'api_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskTalkAPIToken:
    r"""Zendesk service provides two authentication methods. Choose between: `OAuth2.0` or `API token`."""
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""The value of the API token generated. See the <a href=\\"https://docs.airbyte.com/integrations/sources/zendesk-talk\\">docs</a> for more information."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The user email for your Zendesk account."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    AUTH_TYPE: Final[Optional[SourceZendeskTalkAuthType]] = dataclasses.field(default=SourceZendeskTalkAuthType.API_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SourceZendeskTalkAuthentication:
    pass

class SourceZendeskTalkZendeskTalk(str, Enum):
    ZENDESK_TALK = 'zendesk-talk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskTalk:
    r"""The values required to configure the source."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for Zendesk Talk API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    r"""This is your Zendesk subdomain that can be found in your account URL. For example, in https://{MY_SUBDOMAIN}.zendesk.com/, where MY_SUBDOMAIN is the value of your subdomain."""
    SOURCE_TYPE: Final[SourceZendeskTalkZendeskTalk] = dataclasses.field(default=SourceZendeskTalkZendeskTalk.ZENDESK_TALK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Union[SourceZendeskTalkAPIToken, SourceZendeskTalkOAuth20]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Zendesk service provides two authentication methods. Choose between: `OAuth2.0` or `API token`."""
    

