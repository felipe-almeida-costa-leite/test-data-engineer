import dataclasses
from pathlib import PurePath
from .utils import convert_list_string


@dataclasses.dataclass
class S3File:
    path: str


@dataclasses.dataclass
class S3Path(PurePath):
    path: str
    bucket: str
    key: str

    def splited_path(self):
        if self.path.startswith('s3://'):
            self.bucket = self.path.split('s3://')[-1].split('/')[0]
            self.key = convert_list_string(self.path.split('s3://')[-1].split('/')[1:])
        else:
            self.key = convert_list_string(self.path.split('s3://')[-1].split('/'))

