"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class SourceZohoCrmDataCenterLocation(str, Enum):
    r"""Please choose the region of your Data Center location. More info by this <a href=\\"https://www.zoho.com/crm/developer/docs/api/v2/multi-dc.html\\">Link</a>"""
    US = 'US'
    AU = 'AU'
    EU = 'EU'
    IN = 'IN'
    CN = 'CN'
    JP = 'JP'

class SourceZohoCRMZohoCRMEdition(str, Enum):
    r"""Choose your Edition of Zoho CRM to determine API Concurrency Limits"""
    FREE = 'Free'
    STANDARD = 'Standard'
    PROFESSIONAL = 'Professional'
    ENTERPRISE = 'Enterprise'
    ULTIMATE = 'Ultimate'

class SourceZohoCrmEnvironment(str, Enum):
    r"""Please choose the environment"""
    PRODUCTION = 'Production'
    DEVELOPER = 'Developer'
    SANDBOX = 'Sandbox'

class SourceZohoCrmZohoCrm(str, Enum):
    ZOHO_CRM = 'zoho-crm'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZohoCrm:
    r"""The values required to configure the source."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""OAuth2.0 Client ID"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""OAuth2.0 Client Secret"""
    dc_region: SourceZohoCrmDataCenterLocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dc_region') }})
    r"""Please choose the region of your Data Center location. More info by this <a href=\\"https://www.zoho.com/crm/developer/docs/api/v2/multi-dc.html\\">Link</a>"""
    environment: SourceZohoCrmEnvironment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment') }})
    r"""Please choose the environment"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""OAuth2.0 Refresh Token"""
    SOURCE_TYPE: Final[SourceZohoCrmZohoCrm] = dataclasses.field(default=SourceZohoCrmZohoCrm.ZOHO_CRM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    edition: Optional[SourceZohoCRMZohoCRMEdition] = dataclasses.field(default=SourceZohoCRMZohoCRMEdition.FREE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('edition'), 'exclude': lambda f: f is None }})
    r"""Choose your Edition of Zoho CRM to determine API Concurrency Limits"""
    start_datetime: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_datetime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""ISO 8601, for instance: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS+HH:MM`"""
    

