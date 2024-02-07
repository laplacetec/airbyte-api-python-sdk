"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class GoogleWorkspaceAdminReports(str, Enum):
    GOOGLE_WORKSPACE_ADMIN_REPORTS = 'google-workspace-admin-reports'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleWorkspaceAdminReports:
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    r"""The contents of the JSON service account key. See the <a href=\\"https://developers.google.com/admin-sdk/reports/v1/guides/delegation\\">docs</a> for more information on how to generate this key."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The email of the user, which has permissions to access the Google Workspace Admin APIs."""
    lookback: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback'), 'exclude': lambda f: f is None }})
    r"""Sets the range of time shown in the report. Reports API allows from up to 180 days ago."""
    SOURCE_TYPE: Final[GoogleWorkspaceAdminReports] = dataclasses.field(default=GoogleWorkspaceAdminReports.GOOGLE_WORKSPACE_ADMIN_REPORTS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

