"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class NonBreakingSchemaUpdatesBehaviorEnumEnum(str, Enum):
    r"""Set how Airbyte handles syncs when it detects a non-breaking schema change in the source"""
    IGNORE = 'ignore'
    DISABLE_CONNECTION = 'disable_connection'
