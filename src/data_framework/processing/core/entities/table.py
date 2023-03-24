from abc import ABC, abstractmethod, ABCMeta
from .schema import SchemaCatalog, SchemaRaw


class AbstractTable(ABC):
    ...


class TableCatalog(AbstractTable, metaclass=ABCMeta):

    @property
    @abstractmethod
    def table(self):
        ...

    @property
    @abstractmethod
    def database(self):
        ...

    @property
    @abstractmethod
    def schema(self):
        ...


class TableRaw(AbstractTable, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    @abstractmethod
    def path(self):
        ...

    @property
    @abstractmethod
    def partition(self):
        ...

    @property
    @abstractmethod
    def schema(self) -> SchemaRaw:
        ...
