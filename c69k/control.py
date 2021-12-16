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

    @property
    def dataframe(self):
        return self.__cruncher.global_df

    # Private
    def __fetch_files(self) -> "tuple[str]":
        """
        Generates a tuple of absolute paths for every .xls file in the
        `self.__path` directory.
        """
        return tuple(
            os.path.abspath(x) for x in glob(f"{self.__path}/*.xls", recursive=False)
            if re.split(r"\\|/", str(x))[-1][0].isalnum()  # if filename first char is alphanumeric
        )

    # Public
    def dprint(self, msg: str):  # "debug print"
        """Prints if in verbose mode."""
        if self.verbose:
            print(msg)

    def refresh_files(self) -> "tuple[str]":
        """Refreshes the internal file listing and returns it."""
        self.__files = self.__fetch_files()
        return self.files

    def crunch(self):
        """Processes ("crunches") the data in the files pointed by the `files` property."""
        self.__cruncher.compose(self.__files)

    def to_excel(self, filepath_with_name: str):
        """Prints the current global dataframe to an Excel file."""
        # TODO: Fix this (maybe?), doesn't work with .xls files at the moment
        if not filepath_with_name.lower().endswith('.xlsx'):
            filepath_with_name += ".xlsx"

        self.__cruncher.global_df.sort_values(by="Sample Name").to_excel(filepath_with_name, float_format="%.3f", index=False)

    def process(self, filepath_with_name: str):
        """High-level interface function that fetches files, crunches data and prints to excel, all in one."""
        self.refresh_files()
        self.crunch()
        self.to_excel(filepath_with_name)
