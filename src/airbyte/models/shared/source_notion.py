"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional, Union

class SourceNotionSchemasAuthType(str, Enum):
    TOKEN = 'token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNotionAccessToken:
    r"""Choose either OAuth (recommended for Airbyte Cloud) or Access Token. See our <a href='https://docs.airbyte.com/integrations/sources/notion#setup-guide'>docs</a> for more information."""
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""The Access Token for your private Notion integration. See the <a href='https://docs.airbyte.com/integrations/sources/notion#step-1-create-an-integration-in-notion'>docs</a> for more information on how to obtain this token."""
    AUTH_TYPE: Final[SourceNotionSchemasAuthType] = dataclasses.field(default=SourceNotionSchemasAuthType.TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


class SourceNotionAuthType(str, Enum):
    O_AUTH2_0 = 'OAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNotionOAuth20:
    r"""Choose either OAuth (recommended for Airbyte Cloud) or Access Token. See our <a href='https://docs.airbyte.com/integrations/sources/notion#setup-guide'>docs</a> for more information."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The Access Token received by completing the OAuth flow for your Notion integration. See our <a href='https://docs.airbyte.com/integrations/sources/notion#step-2-set-permissions-and-acquire-authorization-credentials'>docs</a> for more information."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Notion integration. See our <a href='https://docs.airbyte.com/integrations/sources/notion#step-2-set-permissions-and-acquire-authorization-credentials'>docs</a> for more information."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Notion integration. See our <a href='https://docs.airbyte.com/integrations/sources/notion#step-2-set-permissions-and-acquire-authorization-credentials'>docs</a> for more information."""
    AUTH_TYPE: Final[SourceNotionAuthType] = dataclasses.field(default=SourceNotionAuthType.O_AUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


class SourceNotionNotion(str, Enum):
    NOTION = 'notion'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNotion:
    r"""The values required to configure the source."""
    credentials: Union[SourceNotionOAuth20, SourceNotionAccessToken] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Choose either OAuth (recommended for Airbyte Cloud) or Access Token. See our <a href='https://docs.airbyte.com/integrations/sources/notion#setup-guide'>docs</a> for more information."""
    SOURCE_TYPE: Final[SourceNotionNotion] = dataclasses.field(default=SourceNotionNotion.NOTION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format YYYY-MM-DDTHH:MM:SS.000Z. During incremental sync, any data generated before this date will not be replicated. If left blank, the start date will be set to 2 years before the present date."""
    

