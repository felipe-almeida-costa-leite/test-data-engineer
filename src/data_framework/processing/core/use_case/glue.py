from src.data_framework.processing.core.entities import SchemaCatalog, Schema, SchemaColum, TableCatalog
from src.data_framework.aws_clients import GlueTable
from src.data_framework.processing.core.use_case.constants import AwsClientsConstants
import dataclasses

REGION = AwsClientsConstants.region.value


@dataclasses.dataclass
class SchemaGlue(SchemaCatalog):
    table: str
    database: str
    schema_glue: Schema = None

    @property
    def schema(self) -> Schema:
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


@dataclasses.dataclass
class TableGlue(TableCatalog):
    table_name: str
    database_name: str
    schema_glue: SchemaGlue = None

    @property
    def table(self):
        return self.table_name

    @property
    def database(self):
        return self.database_name

    @property
    def schema(self) -> Schema:
        if not self.schema_glue:
            self.schema_glue = SchemaGlue(table=self.table, database=self.database)
        return self.schema_glue.schema

    @property
    def schema_dict(self):
        return self.schema.schema_dict()
