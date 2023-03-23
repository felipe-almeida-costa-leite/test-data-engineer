from abc import ABC, abstractmethod, ABCMeta


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
