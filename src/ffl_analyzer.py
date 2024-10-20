import pandas  # can't read tab-delimited CSV files with built-in `csv` module
import pdb
import argparse
import os
import sqlalchemy

# Locals
import ffl_expiration_date_calculator
import ffl_region_lookup
import ffl_district_lookup
import ffl_type_lookup


def get_dataframe(csv_filename) -> pandas.DataFrame:
    return pandas.read_csv(csv_filename, sep="\t").dropna()

def convert_dataframe_to_database(dataframe):
    
    db_engine = sqlalchemy.create_engine(
        f"sqlite:///ffl.sqlite")
    
    dataframe.to_sql(name="ffls", con=db_engine, index=True, index_label="record_id")


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument(
        "-f", "--ffl-file", required=True, type=str, help="The text file from the ATF website")

    argparse_args = argparse_parser.parse_args()

    if not os.path.exists(argparse_args.ffl_file):
        raise FileNotFoundError(
            f"ERROR: File '{argparse_args.ffl_file}' does not exist!")

    ffl_df = get_dataframe(argparse_args.ffl_file)

    print(f"[DEBUG] Loaded dataframe with {len(ffl_df)} rows")

    # Add the date columns..

    expiration_dates_formatted, expiration_days_until = ffl_expiration_date_calculator.calculate_expiration_dates_and_days_remaining(
        ffl_df.LIC_XPRDTE)

    ffl_df["Expiration_Date_Y-M-D"] = pandas.Series(expiration_dates_formatted)

    ffl_df["Days_Until_Expiration"] = pandas.Series(expiration_days_until)

    # Add the other fields

    ffl_df["Region_Name"] = pandas.Series(
        ffl_region_lookup.calculate_country_region(ffl_df.LIC_REGN))

    ffl_df["IRS_District_HQ"] = pandas.Series(
        ffl_district_lookup.lookup_district_names_from_code(ffl_df.LIC_DIST))

    ffl_df["FFL_Type"] = pandas.Series(
        ffl_type_lookup.lookup_ffl_types(ffl_df.LIC_TYPE))

    convert_dataframe_to_database(ffl_df)
