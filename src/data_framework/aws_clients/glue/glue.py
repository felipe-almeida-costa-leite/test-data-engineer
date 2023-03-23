import dataclasses
from ..client_config import ClientConfig
from typing import Dict, List


@dataclasses.dataclass
class GlueTable:
    table_name: str
    database_name: str
    region: str
    endpoint: str = None
    parameters_connection: Dict = None
    properties_table: Dict = None

    @property
    def table(self):
        return self.table_name

    @property
    def database(self):
        return self.database_name

    @property
    def parameters(self):
        return self.parameters_connection

    @property
    def properties(self):
        if not self.properties_table:
            glue = GlueCatalogTable(
                region=self.region,
                endpoint=self.endpoint
            )
            self.parameters.update({'Name': self.table, 'DatabaseName': self.database})
            self.properties_table = glue.get(**self.parameters)
        return self.properties_table

    def partitioned(self) -> bool:
        if not self.properties.get('PartitionKeys'):
            return False
        else:
            return True

    def get_location(self):
        return self.properties.get('StorageDescriptor').get('Location')

    def get_colums_partition(self) -> List:
        response = list()
        if self.partitioned():
            for colum_partition in self.properties.get('PartitionKeys'):
                response.append({'name': colum_partition.get('Name'), 'type': colum_partition.get('Type')})
        return response

    def get_columns(self) -> List[Dict]:
        response = list()
        for columns in self.properties.get('StorageDescriptor').get('Columns'):
            response.append({'name': columns.get('Name'), 'type': columns.get('Type')})
        partitions = self.get_colums_partition()
        if partitions:
            response.extend(partitions)
        return response


@dataclasses.dataclass
class Glue(ClientConfig):

    def __init__(self, region: str = None, endpoint: str = None, **kwargs):
        self.region = region
        self.endpoint = endpoint
        if not kwargs:
            kwargs = {'region': self.region, 'endpoint': self.endpoint, 'service': 'glue'}
        super().__init__(**kwargs)

    def get_table(self, database: str, table: str, **kwargs) -> Dict:
        if not kwargs:
            kwargs = {
                'Name': table,
                'DatabaseName': database
            }
        return self.client.get_object(**kwargs)


@dataclasses.dataclass
class GlueCatalogTable(Glue):

    def __init__(self, region: str = None, endpoint: str = None, **kwargs):
        self.region = region
        self.endpoint = endpoint
        if not kwargs:
            kwargs = {'region': self.region, 'endpoint': self.endpoint, 'service': 'glue'}
        super().__init__(**kwargs)

    def get(self, database: str, table: str, **kwargs) -> Dict:
        if not kwargs:
            kwargs = {
                'Name': table,
                'DatabaseName': database
            }
        return self.get_table(**kwargs).get('Table')
