import os

from pymatic.common.structure import Structure
from pymatic.errors import FileException
from pymatic.litematic.litematic import Litematic


class NBTFile:
    """
    Class for automatically handling file formats.
    """
    def __new__(cls, file_path: str) -> 'Structure':
        match os.path.splitext(file_path)[1]:
            case '.litematic':
                return Litematic.from_file(file_path)
            case _:
                raise FileException(f'Unsupported file type: {file_path}')