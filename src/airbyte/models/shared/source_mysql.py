"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union

class SourceMysqlSchemasMethod(str, Enum):
    STANDARD = 'STANDARD'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMysqlScanChangesWithUserDefinedCursor:
    r"""Incrementally detects new inserts and updates using the <a href=\\"https://docs.airbyte.com/understanding-airbyte/connections/incremental-append/#user-defined-cursor\\">cursor column</a> chosen when configuring a connection (e.g. created_at, updated_at)."""
    METHOD: Final[SourceMysqlSchemasMethod] = dataclasses.field(default=SourceMysqlSchemasMethod.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    


class SourceMysqlMethod(str, Enum):
    CDC = 'CDC'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReadChangesUsingBinaryLogCDC:
    r"""<i>Recommended</i> - Incrementally reads new inserts, updates, and deletes using the MySQL <a href=\\"https://docs.airbyte.com/integrations/sources/mysql/#change-data-capture-cdc\\">binary log</a>. This must be enabled on your database."""
    METHOD: Final[SourceMysqlMethod] = dataclasses.field(default=SourceMysqlMethod.CDC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    initial_waiting_seconds: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initial_waiting_seconds'), 'exclude': lambda f: f is None }})
    r"""The amount of time the connector will wait when it launches to determine if there is new data to sync or not. Defaults to 300 seconds. Valid range: 120 seconds to 1200 seconds. Read about <a href=\\"https://docs.airbyte.com/integrations/sources/mysql/#change-data-capture-cdc\\">initial waiting time</a>."""
    server_time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_time_zone'), 'exclude': lambda f: f is None }})
    r"""Enter the configured MySQL server timezone. This should only be done if the configured timezone in your MySQL instance does not conform to IANNA standard."""
    



@dataclasses.dataclass
class SourceMysqlUpdateMethod:
    pass

class SourceMysqlMysql(str, Enum):
    MYSQL = 'mysql'

class SourceMysqlSchemasSSLModeSSLModesMode(str, Enum):
    VERIFY_IDENTITY = 'verify_identity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VerifyIdentity:
    r"""Always connect with SSL. Verify both CA and Hostname."""
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    MODE: Final[SourceMysqlSchemasSSLModeSSLModesMode] = dataclasses.field(default=SourceMysqlSchemasSSLModeSSLModesMode.VERIFY_IDENTITY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    client_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate'), 'exclude': lambda f: f is None }})
    r"""Client certificate (this is not a required field, but if you want to use it, you will need to add the <b>Client key</b> as well)"""
    client_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key'), 'exclude': lambda f: f is None }})
    r"""Client key (this is not a required field, but if you want to use it, you will need to add the <b>Client certificate</b> as well)"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. This field is optional. If you do not add it - the password will be generated automatically."""
    


class SourceMysqlSchemasSslModeMode(str, Enum):
    VERIFY_CA = 'verify_ca'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMysqlVerifyCA:
    r"""Always connect with SSL. Verifies CA, but allows connection even if Hostname does not match."""
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    MODE: Final[SourceMysqlSchemasSslModeMode] = dataclasses.field(default=SourceMysqlSchemasSslModeMode.VERIFY_CA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    client_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate'), 'exclude': lambda f: f is None }})
    r"""Client certificate (this is not a required field, but if you want to use it, you will need to add the <b>Client key</b> as well)"""
    client_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key'), 'exclude': lambda f: f is None }})
    r"""Client key (this is not a required field, but if you want to use it, you will need to add the <b>Client certificate</b> as well)"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. This field is optional. If you do not add it - the password will be generated automatically."""
    


class SourceMysqlSchemasMode(str, Enum):
    REQUIRED = 'required'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Required:
    r"""Always connect with SSL. If the MySQL server doesn’t support SSL, the connection will not be established. Certificate Authority (CA) and Hostname are not verified."""
    MODE: Final[SourceMysqlSchemasMode] = dataclasses.field(default=SourceMysqlSchemasMode.REQUIRED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    


class SourceMysqlMode(str, Enum):
    PREFERRED = 'preferred'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Preferred:
    r"""Automatically attempt SSL connection. If the MySQL server does not support SSL, continue with a regular connection."""
    MODE: Final[SourceMysqlMode] = dataclasses.field(default=SourceMysqlMode.PREFERRED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    



@dataclasses.dataclass
class SourceMysqlSSLModes:
    pass

class SourceMysqlSchemasTunnelMethodTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMysqlPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[SourceMysqlSchemasTunnelMethodTunnelMethod] = dataclasses.field(default=SourceMysqlSchemasTunnelMethodTunnelMethod.SSH_PASSWORD_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class SourceMysqlSchemasTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMysqlSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[SourceMysqlSchemasTunnelMethod] = dataclasses.field(default=SourceMysqlSchemasTunnelMethod.SSH_KEY_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class SourceMysqlTunnelMethod(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMysqlNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    TUNNEL_METHOD: Final[SourceMysqlTunnelMethod] = dataclasses.field(default=SourceMysqlTunnelMethod.NO_TUNNEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    



@dataclasses.dataclass
class SourceMysqlSSHTunnelMethod:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMysql:
    r"""The values required to configure the source."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The database name."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The host name of the database."""
    replication_method: Union[ReadChangesUsingBinaryLogCDC, SourceMysqlScanChangesWithUserDefinedCursor] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_method') }})
    r"""Configures how data is extracted from the database."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The username which is used to access the database."""
    SOURCE_TYPE: Final[SourceMysqlMysql] = dataclasses.field(default=SourceMysqlMysql.MYSQL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3). For more information read about <a href=\\"https://dev.mysql.com/doc/connector-j/8.0/en/connector-j-reference-jdbc-url-format.html\\">JDBC URL parameters</a>."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""The password associated with the username."""
    port: Optional[int] = dataclasses.field(default=3306, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The port to connect to."""
    ssl_mode: Optional[Union[Preferred, Required, SourceMysqlVerifyCA, VerifyIdentity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})
    r"""SSL connection modes. Read more <a href=\\"https://dev.mysql.com/doc/connector-j/8.0/en/connector-j-reference-using-ssl.html\\"> in the docs</a>."""
    tunnel_method: Optional[Union[SourceMysqlNoTunnel, SourceMysqlSSHKeyAuthentication, SourceMysqlPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

