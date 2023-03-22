from src.data_framework.processing.gateway import *
from typing import *

print(InterfaceFile.create(file_type='YAML')(path='s3'))

