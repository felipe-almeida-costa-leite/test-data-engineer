import dataclasses
from ..concepts.adapter_abstract import AbstractAdapterDataFramework
from importlib import *


@dataclasses.dataclass
class AdapterDataFramework:
    adapter_type: str
    name_class: str = None
    module_class: str = None

    def find_class(self):
        for subclass in AbstractAdapterDataFramework.__subclasses__():
            if self.adapter_type in subclass.__name__:
                self.name_class = subclass.__name__
                self.module_class = subclass.__module__

    @property
    def build(self):
        if not self.module_class or not self.name_class:
            self.find_class()
        module = import_module(self.module_class)
        class_attr = getattr(module, self.name_class)
        return class_attr


class InterfaceAdapter:
    @classmethod
    def create(cls, *args, **kwargs):
        return AdapterDataFramework(*args, **kwargs).build
