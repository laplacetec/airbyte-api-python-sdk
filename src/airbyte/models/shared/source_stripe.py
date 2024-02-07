"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class Stripe(str, Enum):
    STRIPE = 'stripe'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceStripe:
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Your Stripe account ID (starts with 'acct_', find yours <a href=\\"https://dashboard.stripe.com/settings/account\\">here</a>)."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Stripe API key (usually starts with 'sk_live_'; find yours <a href=\\"https://dashboard.stripe.com/apikeys\\">here</a>)."""
    call_rate_limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('call_rate_limit'), 'exclude': lambda f: f is None }})
    r"""The number of API calls per second that you allow connector to make. This value can not be bigger than real API call rate limit (https://stripe.com/docs/rate-limits). If not specified the default maximum is 25 and 100 calls per second for test and production tokens respectively."""
    lookback_window_days: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    r"""When set, the connector will always re-export data from the past N days, where N is the value set here. This is useful if your data is frequently updated after creation. The Lookback Window only applies to streams that do not support event-based incremental syncs: Events, SetupAttempts, ShippingRates, BalanceTransactions, Files, FileLinks, Refunds. More info <a href=\\"https://docs.airbyte.com/integrations/sources/stripe#requirements\\">here</a>"""
    num_workers: Optional[int] = dataclasses.field(default=10, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_workers'), 'exclude': lambda f: f is None }})
    r"""The number of worker thread to use for the sync. The performance upper boundary depends on call_rate_limit setting and type of account."""
    slice_range: Optional[int] = dataclasses.field(default=365, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slice_range'), 'exclude': lambda f: f is None }})
    r"""The time increment used by the connector when requesting data from the Stripe API. The bigger the value is, the less requests will be made and faster the sync will be. On the other hand, the more seldom the state is persisted."""
    SOURCE_TYPE: Final[Stripe] = dataclasses.field(default=Stripe.STRIPE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=dateutil.parser.isoparse('2017-01-25T00:00:00Z'), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Only data generated after this date will be replicated."""
    

