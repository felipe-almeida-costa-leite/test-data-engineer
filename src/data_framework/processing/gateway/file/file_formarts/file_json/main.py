import dataclasses

from ...concepts.file_abstract import GatewayFile


@dataclasses.dataclass
class GatewayFileJSON(GatewayFile):
    ...
