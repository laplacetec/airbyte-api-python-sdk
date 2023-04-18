"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAdsGoogleCredentials:
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Google Ads developer application. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""  
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Google Ads developer application. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""  
    developer_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('developer_token') }})
    r"""Developer token granted by Google to use their APIs. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""  
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining a new access token. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""  
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access Token for making authenticated requests. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAdsCustomQueries:
    
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""A custom defined GAQL query for building the report. Should not contain segments.date expression because it is used by incremental streams. See Google's <a href=\\"https://developers.google.com/google-ads/api/fields/v11/overview_query_builder\\">query builder</a> for more information."""  
    table_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table_name') }})
    r"""The table name in your destination database for choosen query."""  
    
class SourceGoogleAdsGoogleAdsEnum(str, Enum):
    GOOGLE_ADS = 'google-ads'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleAds:
    r"""The values required to configure the source."""
    
    credentials: SourceGoogleAdsGoogleCredentials = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})  
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_id') }})
    r"""Comma separated list of (client) customer IDs. Each customer ID must be specified as a 10-digit number without dashes. More instruction on how to find this value in our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">docs</a>. Metrics streams like AdGroupAdReport cannot be requested for a manager account."""  
    source_type: SourceGoogleAdsGoogleAdsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25. Any data before this date will not be replicated."""  
    conversion_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conversion_window_days'), 'exclude': lambda f: f is None }})
    r"""A conversion window is the period of time after an ad interaction (such as an ad click or video view) during which a conversion, such as a purchase, is recorded in Google Ads. For more information, see Google's <a href=\\"https://support.google.com/google-ads/answer/3123169?hl=en\\">documentation</a>."""  
    custom_queries: Optional[list[SourceGoogleAdsCustomQueries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_queries'), 'exclude': lambda f: f is None }})  
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25. Any data after this date will not be replicated."""  
    login_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('login_customer_id'), 'exclude': lambda f: f is None }})
    r"""If your access to the customer account is through a manager account, this field is required and must be set to the customer ID of the manager account (10-digit number without dashes). More information about this field you can see <a href=\\"https://developers.google.com/google-ads/api/docs/concepts/call-structure#cid\\">here</a>"""  
    