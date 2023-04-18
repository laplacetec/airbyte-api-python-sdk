"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class DestinationConvexConvexEnum(str, Enum):
    CONVEX = 'convex'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationConvex:
    r"""The values required to configure the destination."""
    
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key') }})
    r"""API access key used to send data to a Convex deployment."""  
    deployment_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployment_url') }})
    r"""URL of the Convex deployment that is the destination"""  
    destination_type: DestinationConvexConvexEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})  
    