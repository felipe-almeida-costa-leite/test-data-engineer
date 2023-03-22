import dataclasses

from ...concepts.file_abstract import GatewayFile
from typing import *
from ......aws_clients.s3 import S3File
from ......utils.utils import read_raw_file_from_dictory
from .schema.schema_control import YAMLSchemaVersions
from yaml import safe_load
import yamale
from .....adapter.main.main import InterfaceAdapter


@dataclasses.dataclass
class GatewayFileYAML(GatewayFile):
    path: str
    file_content: Dict = None

    @property
    def read_file(self) -> str:
        return S3File(region='sa-east-1').get(path=self.path)

    @property
    def read_schema(self) -> str:
        return read_raw_file_from_dictory(
            path=YAMLSchemaVersions.get_schema_path(schema_version=self.file.get('version')))

    @property
    def file(self) -> Dict:
        return safe_load(self.read_file)

    @property
    def schema(self) -> Dict:
        return safe_load(self.read_schema)

    @property
    def validated(self):
        if yamale.validate(schema=self.schema, data=self.file):
            return True
        else:
            return False

    def run(self):
        InterfaceAdapter.create('File')(**self.file).run()
