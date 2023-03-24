from __future__ import annotations
from abc import ABC, abstractmethod, ABCMeta
import dataclasses
from typing import List


class AbstractSchema(ABC):
    ...


class SchemaCatalog(AbstractSchema, metaclass=ABCMeta):

    @property
    @abstractmethod
    def schema(self):
        ...


class SchemaRaw(AbstractSchema, metaclass=ABCMeta):

    @property
    @abstractmethod
    def schema(self):
        ...


@dataclasses.dataclass
class SchemaColum:
    name: str
    type: str
    index: int


@dataclasses.dataclass
class Schema:
    schema: List[SchemaColum]
