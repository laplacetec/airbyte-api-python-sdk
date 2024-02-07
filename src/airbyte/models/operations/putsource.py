"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import sourceputrequest as shared_sourceputrequest
from ...models.shared import sourceresponse as shared_sourceresponse
from typing import Optional


@dataclasses.dataclass
class PutSourceRequest:
    source_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    source_put_request: Optional[shared_sourceputrequest.SourcePutRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutSourceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    source_response: Optional[shared_sourceresponse.SourceResponse] = dataclasses.field(default=None)
    r"""Update a source and fully overwrite it"""
    

