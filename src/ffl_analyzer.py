import pandas # can't read tab-delimited CSV files with built-in `csv` module
import pdb



def get_dataframe(csv_filename) -> pandas.DataFrame:
    return pandas.read_csv(csv_filename, sep="\t")


def generate_ffl_expiration_dates()


if __name__ == "__main__":

    csv_path = "../original/0924-ffl-list-complete.txt"

    ffl_df = get_dataframe(csv_path)

    import pdb; pdb.set_trace()

    print(f"Loaded dataframe with columns: {ffl_df.columns}")



    