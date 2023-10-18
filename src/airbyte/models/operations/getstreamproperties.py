"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import streampropertiesresponse as shared_streampropertiesresponse
from typing import Optional


@dataclasses.dataclass
class GetStreamPropertiesRequest:
    destination_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'destinationId', 'style': 'form', 'explode': True }})
    r"""ID of the destination"""
    source_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceId', 'style': 'form', 'explode': True }})
    r"""ID of the source"""
    ignore_cache: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'ignoreCache', 'style': 'form', 'explode': True }})
    r"""If true pull the latest schema from the source, else pull from cache (default false)"""
    



@dataclasses.dataclass
class GetStreamPropertiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    stream_properties_response: Optional[shared_streampropertiesresponse.StreamPropertiesResponse] = dataclasses.field(default=None)
    r"""Get the available streams properties for a source/destination pair."""
    

