import os

from datetime import datetime

import pandas as pd

from c69k.control import Crunchinator69k

if __name__ == "__main__":
    filepath = "/rhome/leo/Desktop"
    proc = Crunchinator69k(path=filepath, verbose=True)
    default_outfile = f"{os.path.dirname(os.path.realpath(__file__))}"
    default_outfile += f"/{datetime.now().strftime(r'%b-%d-%Y_%H-%M-%S').lower()}.xls"

    # proc.process(default_outfile)
    proc.refresh_files()
    proc.crunch()
    print(proc.dataframe)
