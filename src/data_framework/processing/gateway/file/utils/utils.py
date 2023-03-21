from typing import List


def convert_list_string(lista: List, sep='/'):
    key = str()
    for index, value in enumerate(lista):
        if value == lista[-1]:
            key += str(value)
        else:
            key += str(value) + sep
    return key
