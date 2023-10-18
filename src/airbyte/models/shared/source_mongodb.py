"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, Final, Optional, Union

class SourceMongodbMongoDBInstanceTypeMongoDBAtlasInstance(str, Enum):
    ATLAS = 'atlas'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbMongoDBInstanceTypeMongoDBAtlas:
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    cluster_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster_url') }})
    r"""The URL of a cluster to connect to."""
    INSTANCE: Final[SourceMongodbMongoDBInstanceTypeMongoDBAtlasInstance] = dataclasses.field(default=SourceMongodbMongoDBInstanceTypeMongoDBAtlasInstance.ATLAS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    


class SourceMongodbMongoDbInstanceTypeReplicaSetInstance(str, Enum):
    REPLICA = 'replica'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbMongoDbInstanceTypeReplicaSet:
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    server_addresses: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_addresses') }})
    r"""The members of a replica set. Please specify `host`:`port` of each member separated by comma."""
    INSTANCE: Final[SourceMongodbMongoDbInstanceTypeReplicaSetInstance] = dataclasses.field(default=SourceMongodbMongoDbInstanceTypeReplicaSetInstance.REPLICA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    replica_set: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replica_set'), 'exclude': lambda f: f is None }})
    r"""A replica set in MongoDB is a group of mongod processes that maintain the same data set."""
    


class SourceMongodbMongoDbInstanceTypeStandaloneMongoDbInstanceInstance(str, Enum):
    STANDALONE = 'standalone'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbMongoDbInstanceTypeStandaloneMongoDbInstance:
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The host name of the Mongo database."""
    INSTANCE: Final[SourceMongodbMongoDbInstanceTypeStandaloneMongoDbInstanceInstance] = dataclasses.field(default=SourceMongodbMongoDbInstanceTypeStandaloneMongoDbInstanceInstance.STANDALONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    port: Optional[int] = dataclasses.field(default=27017, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The port of the Mongo database."""
    



@dataclasses.dataclass
class SourceMongodbMongoDbInstanceType:
    pass

class SourceMongodbMongodb(str, Enum):
    MONGODB = 'mongodb'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodb:
    r"""The values required to configure the source."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The database you want to replicate."""
    SOURCE_TYPE: Final[SourceMongodbMongodb] = dataclasses.field(default=SourceMongodbMongodb.MONGODB, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    auth_source: Optional[str] = dataclasses.field(default='admin', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_source'), 'exclude': lambda f: f is None }})
    r"""The authentication source where the user information is stored."""
    instance_type: Optional[Union[SourceMongodbMongoDbInstanceTypeStandaloneMongoDbInstance, SourceMongodbMongoDbInstanceTypeReplicaSet, SourceMongodbMongoDBInstanceTypeMongoDBAtlas]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_type'), 'exclude': lambda f: f is None }})
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""The password associated with this username."""
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""The username which is used to access the database."""
    

