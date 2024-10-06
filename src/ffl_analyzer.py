import pandas # can't read tab-delimited CSV files with built-in `csv` module
import pdb

if __name__ == "__main__":

    csv_path = "../original/0924-ffl-list-complete.txt"
    df = pandas.read_csv(csv_path, sep="\t")
    pdb.set_trace()