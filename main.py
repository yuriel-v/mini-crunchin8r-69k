import os

from datetime import datetime

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
            proc = Crunchinator69k(path=reports_path, verbose=True)
            reports_path = os.path.abspath(reports_path)
            print(f"Using '{reports_path}' as path.\n")

            proc.refresh_files()
            proc.crunch()

            print("-" * 82)  # len of print below
            print("All files processed. Please input the file name (optionally a path to a new file).")
            default_outfile = f"{os.path.dirname(os.path.realpath(__file__))}"
            default_outfile += '/' if '/' in default_outfile else '\\'
            default_outfile += f"{datetime.now().strftime(r'%b-%d-%Y_%H-%M-%S').lower()}.xlsx"
            outfile = input(f"Default is '{default_outfile}'.\n>> ")

            print("-" * (len(outfile) + 3))
            outfile = os.path.abspath(outfile) if outfile else default_outfile
            print(f"Printing to '{outfile}'.")
            proc.to_excel(outfile)
            print("All done. Terminating.")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Terminating.")
        exit(0)
