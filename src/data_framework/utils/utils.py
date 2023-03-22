from typing import List, Union
from pathlib import Path


def convert_list_string(lista: List, sep='/'):
    key = str()
    for index, value in enumerate(lista):
        if value == lista[-1]:
            key += str(value)
        else:
            key += str(value) + sep
    return key


def read_raw_file_from_dictory(path: Union[Path, str]):
    if isinstance(path, str):
        path = Path(path)
    with open(path) as file:
        return file.read()
