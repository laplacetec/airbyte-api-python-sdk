"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional

class PeriodUsedForMostPopularStreams(int, Enum):
    r"""Period of time (in days)"""
    ONE = 1
    SEVEN = 7
    THIRTY = 30

class ShareTypeUsedForMostPopularSharedStream(str, Enum):
    r"""Share Type"""
    FACEBOOK = 'facebook'

class Nytimes(str, Enum):
    NYTIMES = 'nytimes'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNytimes:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    period: PeriodUsedForMostPopularStreams = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period') }})
    r"""Period of time (in days)"""
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Start date to begin the article retrieval (format YYYY-MM)"""
    SOURCE_TYPE: Final[Nytimes] = dataclasses.field(default=Nytimes.NYTIMES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""End date to stop the article retrieval (format YYYY-MM)"""
    share_type: Optional[ShareTypeUsedForMostPopularSharedStream] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('share_type'), 'exclude': lambda f: f is None }})
    r"""Share Type"""
    

