import dataclasses
from typing import Dict

import boto3


@dataclasses.dataclass
class ClientConfig:
    service: str
    region: str
    endpoint: str = None
    session_parameters: Dict = None

    @property
    def parameters(self):
        if not self.session_parameters:
            if self.endpoint:
                self.session_parameters = {
                    'endpoint_url': self.endpoint,
                    'service_name': self.service,
                    'region_name': self.region
                }
            else:
                self.session_parameters = {
                    'service_name': self.service,
                    'region_name': self.region
                }
        return self.session_parameters

    @property
    def client(self) -> boto3.client:
        return boto3.client(**self.parameters)

    @property
    def resource(self) -> boto3.resource:
        return boto3.resource(**self.parameters)
