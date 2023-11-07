"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Union

class SourceHubspotSchemasAuthType(str, Enum):
    r"""Name of the credentials set"""
    PRIVATE_APP_CREDENTIALS = 'Private App Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PrivateApp:
    r"""Choose how to authenticate to HubSpot."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""HubSpot Access token. See the <a href=\\"https://developers.hubspot.com/docs/api/private-apps\\">Hubspot docs</a> if you need help finding this token."""
    CREDENTIALS_TITLE: Final[SourceHubspotSchemasAuthType] = dataclasses.field(default=SourceHubspotSchemasAuthType.PRIVATE_APP_CREDENTIALS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    r"""Name of the credentials set"""
    


class SourceHubspotAuthType(str, Enum):
    r"""Name of the credentials"""
    O_AUTH_CREDENTIALS = 'OAuth Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspotOAuth:
    r"""Choose how to authenticate to HubSpot."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your HubSpot developer application. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this ID."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret for your HubSpot developer application. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this secret."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh token to renew an expired access token. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this token."""
    CREDENTIALS_TITLE: Final[SourceHubspotAuthType] = dataclasses.field(default=SourceHubspotAuthType.O_AUTH_CREDENTIALS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    r"""Name of the credentials"""
    



@dataclasses.dataclass
class SourceHubspotAuthentication:
    pass

class SourceHubspotHubspot(str, Enum):
    HUBSPOT = 'hubspot'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspot:
    r"""The values required to configure the source."""
    credentials: Union[SourceHubspotOAuth, PrivateApp] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Choose how to authenticate to HubSpot."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[SourceHubspotHubspot] = dataclasses.field(default=SourceHubspotHubspot.HUBSPOT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

