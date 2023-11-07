"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Final, Optional, Union

class SourceHarvestSchemasAuthType(str, Enum):
    TOKEN = 'Token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHarvestAuthenticateWithPersonalAccessToken:
    r"""Choose how to authenticate to Harvest."""
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Log into Harvest and then create new <a href=\\"https://id.getharvest.com/developers\\"> personal access token</a>."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    AUTH_TYPE: Final[Optional[SourceHarvestSchemasAuthType]] = dataclasses.field(default=SourceHarvestSchemasAuthType.TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceHarvestAuthType(str, Enum):
    CLIENT = 'Client'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaHarvestOAuth:
    r"""Choose how to authenticate to Harvest."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Harvest developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Harvest developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh Token to renew the expired Access Token."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    AUTH_TYPE: Final[Optional[SourceHarvestAuthType]] = dataclasses.field(default=SourceHarvestAuthType.CLIENT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SourceHarvestAuthenticationMechanism:
    pass

class SourceHarvestHarvest(str, Enum):
    HARVEST = 'harvest'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHarvest:
    r"""The values required to configure the source."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Harvest account ID. Required for all Harvest requests in pair with Personal Access Token"""
    replication_start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[SourceHarvestHarvest] = dataclasses.field(default=SourceHarvestHarvest.HARVEST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Union[AuthenticateViaHarvestOAuth, SourceHarvestAuthenticateWithPersonalAccessToken]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Harvest."""
    replication_end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data after this date will not be replicated."""
    

