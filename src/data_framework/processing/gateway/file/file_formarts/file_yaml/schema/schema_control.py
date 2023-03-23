from enum import Enum
from pathlib import Path


class YAMLSchemaVersions(Enum):
    v0 = "v0.yaml"

    @classmethod
    def get_version(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def get_schema_path(cls, schema_version: str = 'v0'):
        root = Path(__file__).parent
        path = Path('versions')
        versions = cls.get_version()
        if schema_version in versions:
            return root / path / str(cls[schema_version].value)
