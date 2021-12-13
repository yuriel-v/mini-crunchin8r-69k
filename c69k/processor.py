from typing import Iterable, Union
import pandas as pd


class Processor69k:
    def __init__(self):
        self.global_df = pd.DataFrame()

    # Private
    def __extract(self, file: str):
        """Extracts information from `file` into the global dataframe."""

    # Public
    def compose(self, file: Union[str, Iterable]) -> None:
        """
        Composes the global dataframe, extracting information from the file(s)
        given in `file`.
        """
        if isinstance(file, str):
            # extract once
            pass
        elif isinstance(file, Iterable):
            # loop extractions for filename in file
            pass
        else:
            raise TypeError("Expected file string or iterable, got neither")
