import dataclasses
from typing import Dict

from ...concepts.adapter_abstract import AbstractAdapterDataFramework
from jsonschema import validate
from ..schema import *


@dataclasses.dataclass
class AdapterFile(AbstractAdapterDataFramework):
    data_file: Dict

    def validate_source(self):
        validate(instance=self.data_file.get('source'), schema=JsonSchemaSource.schema.value)
        return True

    def validate_load(self):
        validate(instance=self.data_file.get('load'), schema=JsonSchemaLoad.schema.value)
        return True

    def validate_target(self):
        validate(instance=self.data_file.get('target'), schema=JsonSchemaTarget.schema.value)
        return True

    def validated(self):
        try:
            for validators in [self.validate_source, self.validate_load, self.validate_target]:
                validators()
            return True
        except Exception as err:
            raise err

    def run(self):
        ...
