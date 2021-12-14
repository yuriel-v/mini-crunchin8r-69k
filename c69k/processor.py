from typing import Iterable, Union
import pandas as pd


class Processor69k:
    def __init__(self, verbose: bool = True):
        self.global_df = pd.DataFrame()
        self.__relevant_columns = {
            "variable": ("CT", "Quantity"),  # vary with well position
            "constant": ("Ct Mean", "Ct SD", "Quantity Mean", "Quantity SD")  # constant across positions
        }
        self.verbose = verbose

    # Private
    def __extract(self, file: str):
        """Extracts information from `file` into the global dataframe. Must be an excel file."""
        df = pd.read_excel(file, usecols="B,D:E,I:N", header=42)
        self.dprint(f"Matched: {file}")

        samples = df["Sample Name"].unique()
        targets = df["Target Name"].unique()

        for sample in samples:
            value_delim = "="
            pair_delim = ";"
            new_row = {"Sample Name": sample}

            for target in targets:
                subset = df.loc[(df["Sample Name"] == sample) & (df["Target Name"] == target)]

                for col in self.__relevant_columns["constant"]:
                    new_row[f"{col}-{target}"] = subset.iloc[0][col]

                for col in self.__relevant_columns["variable"]:
                    new_row[f"{col}-{target}"] = pair_delim.join([
                        f'{subset.iloc[x]["Well Position"]}{value_delim}{subset.iloc[x][col]}'
                        for x in range(len(subset))
                    ])
                    # ex. {"CT-ibeA": "A1=1.22;A2=2.44", "Quantity-ibeA": "A1=3.66;A2=3.66"}

            self.global_df = self.global_df.append(new_row, ignore_index=True)

    # Public
    def dprint(self, msg: str):  # "debug print"
        """Prints if in verbose mode."""
        if self.verbose:
            print(msg)

    def compose(self, file: Union[str, Iterable]) -> None:
        """
        Composes the global dataframe, extracting information from the file(s)
        given in `file`.
        """
        if isinstance(file, str):
            self.__extract(file)
        elif isinstance(file, Iterable):
            for filename in file:
                self.__extract(filename)
        else:
            raise TypeError("Expected file string or iterable, got neither")
