"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Final, List, Optional, Union

class SourceSurveySparrowBaseURLGlobalAccountURLBase(str, Enum):
    HTTPS_API_SURVEYSPARROW_COM_V3 = 'https://api.surveysparrow.com/v3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrowBaseURLGlobalAccount:
    r"""Is your account location is EU based? If yes, the base url to retrieve data will be different."""
    URL_BASE: Final[Optional[SourceSurveySparrowBaseURLGlobalAccountURLBase]] = dataclasses.field(default=SourceSurveySparrowBaseURLGlobalAccountURLBase.HTTPS_API_SURVEYSPARROW_COM_V3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    


class SourceSurveySparrowBaseURLEUBasedAccountURLBase(str, Enum):
    HTTPS_EU_API_SURVEYSPARROW_COM_V3 = 'https://eu-api.surveysparrow.com/v3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrowBaseURLEUBasedAccount:
    r"""Is your account location is EU based? If yes, the base url to retrieve data will be different."""
    URL_BASE: Final[Optional[SourceSurveySparrowBaseURLEUBasedAccountURLBase]] = dataclasses.field(default=SourceSurveySparrowBaseURLEUBasedAccountURLBase.HTTPS_EU_API_SURVEYSPARROW_COM_V3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SourceSurveySparrowBaseURL:
    pass

class SourceSurveySparrowSurveySparrow(str, Enum):
    SURVEY_SPARROW = 'survey-sparrow'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrow:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Your access token. See <a href=\\"https://developers.surveysparrow.com/rest-apis#authentication\\">here</a>. The key is case sensitive."""
    SOURCE_TYPE: Final[SourceSurveySparrowSurveySparrow] = dataclasses.field(default=SourceSurveySparrowSurveySparrow.SURVEY_SPARROW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    region: Optional[Union[SourceSurveySparrowBaseURLEUBasedAccount, SourceSurveySparrowBaseURLGlobalAccount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Is your account location is EU based? If yes, the base url to retrieve data will be different."""
    survey_id: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_id'), 'exclude': lambda f: f is None }})
    r"""A List of your survey ids for survey-specific stream"""
    

