from __future__ import annotations

import dataclasses
from typing import List


@dataclasses.dataclass
class SchemaColum:
    name: str
    type: str
    index: int


@dataclasses.dataclass
class Schema:
    schema: List[SchemaColum]

