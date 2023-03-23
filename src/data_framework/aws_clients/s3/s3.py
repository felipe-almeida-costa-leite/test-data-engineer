import dataclasses
from ...utils.utils import convert_list_string
from ..client_config import ClientConfig
from .constants import S3Constants
from typing import *


@dataclasses.dataclass
class S3Path:
    path: str
    bucket_path: str = None
    key_path: str = None

    def splited_path(self):
        if self.path.startswith('s3://'):
            self.bucket_path = self.path.split('s3://')[-1].split('/')[0]
            self.key_path = convert_list_string(self.path.split('s3://')[-1].split('/')[1:])
        else:
            splited_list = self.path.split('/')
            self.bucket_path = splited_list[0]
            self.key_path = convert_list_string(splited_list[1:])

    @property
    def bucket(self):
        if not self.bucket_path:
            self.splited_path()
        return self.bucket_path

    @property
    def key(self):
        if not self.key_path:
            self.splited_path()
        return self.key_path


@dataclasses.dataclass
class S3(ClientConfig):

    def __init__(self, region: str = None, endpoint: str = None, **kwargs):
        self.region = region
        self.endpoint = endpoint
        if not kwargs:
            kwargs = {'region': self.region, 'endpoint': self.endpoint, 'service': 's3'}
        super().__init__(**kwargs)

    def get_object(self, path: Union[S3Path, str], **kwargs) -> Dict:
        if not kwargs:
            if isinstance(path, str):
                path = S3Path(path=path)
            kwargs = {
                'bucket': path.bucket,
                'key': path.key
            }
        return self.client.get_object(**kwargs)


@dataclasses.dataclass
class S3File(S3):

    def __init__(self, region: str = None, endpoint: str = None, **kwargs):
        self.region = region
        self.endpoint = endpoint
        if not kwargs:
            kwargs = {'region': self.region, 'endpoint': self.endpoint, 'service': 's3'}
        super().__init__(**kwargs)

    def get(self, path: Union[S3Path, str], *, enconding: Optional[str] = None):
        response = self.get_object(path=path).get('Body')
        if not response:
            return dict()
        else:
            if not enconding:
                enconding = S3Constants.DEFAULT_ENCONDING.value
            return response.read().decode(enconding=enconding)
