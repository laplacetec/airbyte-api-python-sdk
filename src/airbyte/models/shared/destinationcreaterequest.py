"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .destination_aws_datalake import DestinationAwsDatalake
from .destination_azure_blob_storage import DestinationAzureBlobStorage
from .destination_bigquery import DestinationBigquery
from .destination_bigquery_denormalized import DestinationBigqueryDenormalized
from .destination_clickhouse import DestinationClickhouse
from .destination_convex import DestinationConvex
from .destination_cumulio import DestinationCumulio
from .destination_databend import DestinationDatabend
from .destination_databricks import DestinationDatabricks
from .destination_dev_null import DestinationDevNull
from .destination_dynamodb import DestinationDynamodb
from .destination_elasticsearch import DestinationElasticsearch
from .destination_firebolt import DestinationFirebolt
from .destination_firestore import DestinationFirestore
from .destination_gcs import DestinationGcs
from .destination_google_sheets import DestinationGoogleSheets
from .destination_keen import DestinationKeen
from .destination_kinesis import DestinationKinesis
from .destination_langchain import DestinationLangchain
from .destination_milvus import DestinationMilvus
from .destination_mongodb import DestinationMongodb
from .destination_mssql import DestinationMssql
from .destination_mysql import DestinationMysql
from .destination_oracle import DestinationOracle
from .destination_pinecone import DestinationPinecone
from .destination_postgres import DestinationPostgres
from .destination_pubsub import DestinationPubsub
from .destination_redis import DestinationRedis
from .destination_redshift import DestinationRedshift
from .destination_s3 import DestinationS3
from .destination_s3_glue import DestinationS3Glue
from .destination_sftp_json import DestinationSftpJSON
from .destination_snowflake import DestinationSnowflake
from .destination_timeplus import DestinationTimeplus
from .destination_typesense import DestinationTypesense
from .destination_vertica import DestinationVertica
from .destination_xata import DestinationXata
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationCreateRequest:
    configuration: Union[DestinationAwsDatalake, DestinationAzureBlobStorage, DestinationBigquery, DestinationBigqueryDenormalized, DestinationClickhouse, DestinationConvex, DestinationCumulio, DestinationDatabend, DestinationDatabricks, DestinationDevNull, DestinationDynamodb, DestinationElasticsearch, DestinationFirebolt, DestinationFirestore, DestinationGcs, DestinationGoogleSheets, DestinationKeen, DestinationKinesis, DestinationLangchain, DestinationMilvus, DestinationMongodb, DestinationMssql, DestinationMysql, DestinationOracle, DestinationPinecone, DestinationPostgres, DestinationPubsub, DestinationRedis, DestinationRedshift, DestinationS3, DestinationS3Glue, DestinationSftpJSON, DestinationSnowflake, DestinationTimeplus, DestinationTypesense, DestinationVertica, DestinationXata] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The values required to configure the destination."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    

