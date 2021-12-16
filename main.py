import os

from datetime import datetime
from pathlib import Path

from c69k.control import Crunchinator69k

if __name__ == "__main__":
    try:
        print("Starting mini-crunchinator 69k.")
        print("Note: Press CTRL+C anytime to terminate.")
        print("-" * 40)  # len of previous print
        print("Please input a path to read from. Entering an empty value terminates the program.")
        reports_path = input("WARNING: Subdirectories will not be searched!\n>> ")

        if not reports_path:
            print("Terminating...")

        else:
            print("-" * (len(reports_path) + 3))
            reports_path = Path(reports_path).resolve()
            proc = Crunchinator69k(path=reports_path, verbose=True)
            print(f"Using '{reports_path}' as path.\n")

            proc.refresh_files()
            proc.crunch()

            print("-" * 82)  # len of print below
            print("All files processed. Please input the file name (optionally a path to a new file).")
            default_outfile = f"{Path(__file__).parent.resolve()}"
            default_outfile += '/' if '/' in default_outfile else '\\'
            default_outfile += f"{datetime.now().strftime(r'%b-%d-%Y_%H-%M-%S').lower()}.xlsx"
            outfile = input(f"Default is '{default_outfile}'.\n>> ")

            print("-" * (len(outfile) + 3))
            outfile = Path(outfile).resolve() if outfile else default_outfile
            print(f"Printing to '{outfile}'.")
            proc.to_excel(outfile)
            print("All done. Terminating.")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Terminating.")
        exit(0)
