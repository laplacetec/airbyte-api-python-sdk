"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import workspaceresponse as shared_workspaceresponse
from ..shared import workspaceupdaterequest as shared_workspaceupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateWorkspaceRequest:
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    workspace_update_request: shared_workspaceupdaterequest.WorkspaceUpdateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateWorkspaceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    workspace_response: Optional[shared_workspaceresponse.WorkspaceResponse] = dataclasses.field(default=None)
    r"""Successful operation"""
    

