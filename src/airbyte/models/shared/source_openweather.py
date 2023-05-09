"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceOpenweatherLanguageEnum(str, Enum):
    r"""You can use lang parameter to get the output in your language. The contents of the description field will be translated. See <a href=\\"https://openweathermap.org/api/one-call-api#multi\\">here</a> for the list of supported languages."""
    AF = 'af'
    AL = 'al'
    AR = 'ar'
    AZ = 'az'
    BG = 'bg'
    CA = 'ca'
    CZ = 'cz'
    DA = 'da'
    DE = 'de'
    EL = 'el'
    EN = 'en'
    EU = 'eu'
    FA = 'fa'
    FI = 'fi'
    FR = 'fr'
    GL = 'gl'
    HE = 'he'
    HI = 'hi'
    HR = 'hr'
    HU = 'hu'
    ID = 'id'
    IT = 'it'
    JA = 'ja'
    KR = 'kr'
    LA = 'la'
    LT = 'lt'
    MK = 'mk'
    NO = 'no'
    NL = 'nl'
    PL = 'pl'
    PT = 'pt'
    PT_BR = 'pt_br'
    RO = 'ro'
    RU = 'ru'
    SV = 'sv'
    SE = 'se'
    SK = 'sk'
    SL = 'sl'
    SP = 'sp'
    ES = 'es'
    SR = 'sr'
    TH = 'th'
    TR = 'tr'
    UA = 'ua'
    UK = 'uk'
    VI = 'vi'
    ZH_CN = 'zh_cn'
    ZH_TW = 'zh_tw'
    ZU = 'zu'

class SourceOpenweatherOpenweatherEnum(str, Enum):
    OPENWEATHER = 'openweather'

class SourceOpenweatherUnitsEnum(str, Enum):
    r"""Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default."""
    STANDARD = 'standard'
    METRIC = 'metric'
    IMPERIAL = 'imperial'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOpenweather:
    r"""The values required to configure the source."""
    
    appid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appid') }})
    r"""Your OpenWeather API Key. See <a href=\\"https://openweathermap.org/api\\">here</a>. The key is case sensitive."""
    lat: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lat') }})
    r"""Latitude for which you want to get weather condition from. (min -90, max 90)"""
    lon: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lon') }})
    r"""Longitude for which you want to get weather condition from. (min -180, max 180)"""
    source_type: SourceOpenweatherOpenweatherEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    lang: Optional[SourceOpenweatherLanguageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lang'), 'exclude': lambda f: f is None }})
    r"""You can use lang parameter to get the output in your language. The contents of the description field will be translated. See <a href=\\"https://openweathermap.org/api/one-call-api#multi\\">here</a> for the list of supported languages."""
    units: Optional[SourceOpenweatherUnitsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('units'), 'exclude': lambda f: f is None }})
    r"""Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default."""
    