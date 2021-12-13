import os
import re

from glob import glob

from c69k.processor import Processor69k


class Crunchinator69k:
    def __init__(self, path: str, verbose: bool = True):
        self.verbose = verbose
        self.__path = os.path.abspath(re.sub(r"\\|/$", "", path))
        self.__files = self.__fetch_files()
        self.__cruncher = Processor69k()

    # Properties
    @property
    def files(self):
        return self.__files

    # Private
    def __fetch_files(self) -> tuple[str]:
        """
        Generates a tuple of absolute paths for every .xls file in the
        `self.__path` directory.
        """
        return tuple(
            os.path.abspath(x) for x in glob(f"{self.__path}/*.xls", recursive=False)
            if re.split(r"\\|/", str(x))[-1][0].isalnum()  # if filename first char is alphanumeric
        )

    # Public
    def refresh_files(self) -> tuple(str):
        """Refreshes the internal file listing and returns it."""
        self.__files = self.__fetch_files()
        return self.files
