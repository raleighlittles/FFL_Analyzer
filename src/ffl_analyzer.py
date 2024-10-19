import pandas # can't read tab-delimited CSV files with built-in `csv` module
import pdb
import datetime
import csv

# Locals
import ffl_expiration_date_calculator
import ffl_region_lookup
import ffl_district_lookup
import ffl_type_lookup

def get_dataframe(csv_filename) -> pandas.DataFrame:
    return pandas.read_csv(csv_filename, sep="\t")


if __name__ == "__main__":

    csv_path = "../original/0924-ffl-list-complete.txt"

    ffl_df = get_dataframe(csv_path)

    # Add the date columns..

    expiration_dates_formatted, expiration_days_until = ffl_expiration_date_calculator.calculate_expiration_dates_and_days_remaining(ffl_df.LIC_XPRDTE)

    ffl_df["Expiration_Date_Y-M-D"] = pandas.Series(expiration_dates_formatted)

    ffl_df["Days_Until_Expiration"] = pandas.Series(expiration_days_until)

    # Add the other fields

    ffl_df["Region_Name"] = pandas.Series(ffl_region_lookup.calculate_country_region(ffl_df.LIC_REGN))

    ffl_df["IRS_District_HQ"] = pandas.Series(ffl_district_lookup.lookup_district_names_from_code(ffl_df.LIC_DIST))
    
    ffl_df["FFL_Type"] = pandas.Series(ffl_type_lookup.lookup_ffl_types(ffl_df.LIC_TYPE))

    pdb.set_trace()