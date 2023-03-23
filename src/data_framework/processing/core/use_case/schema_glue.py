from ..entities import SchemaCatalog, Schema, SchemaColum
from src.data_framework.aws_clients import GlueTable
from .constants import AwsClientsConstants
import dataclasses

REGION = AwsClientsConstants.region.value


@dataclasses.dataclass
class SchemaGlue(SchemaCatalog):
    schema_glue: Schema = None
    table: str = None
    database: str = None

    @property
    def schema(self):
        if not self.schema_glue:
            self.schema_glue = self.collect_schema()
        return self.schema

    def collect_schema(self) -> Schema:
        response = list()
        for index, colum in enumerate(
                GlueTable(region=REGION, table_name=self.table, database_name=self.database).get_columns()):
            response.append(
                SchemaColum(
                    name=colum.get('name'),
                    type=colum.get('type'),
                    index=index
                )
            )
        return Schema(schema=response)
