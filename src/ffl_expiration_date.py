import datetime
import csv
import time

def load_month_codes(month_code_filename) -> dict:

    month_codes = dict()

    with open(month_code_filename, mode='r') as month_code_csv_file_obj:
        csv_reader = csv.reader(month_code_csv_file_obj)
        
        for row in csv_reader:
            month_codes[row[0].strip()] = row[1].strip()

    return month_codes

def calculate_days_until_ffl_expiration(ffl_expiration_month, ffl_expiration_year):

    ffl_expiration_month_as_int = int(time.strptime(ffl_expiration_month, "%B").tm_mon)

    return (datetime.datetime(year=ffl_expiration_year, month=ffl_expiration_month_as_int, day=1) - datetime.datetime.now()).days



def calculate_expiration_year(ffl_expiration_year_last_num) -> int:

    curr_year = datetime.datetime.now().year

    ffl_expiration_year = 0

    if (int(str(curr_year)[-1]) < ffl_expiration_year_last_num):
        # The FFL expires in the same decade that we're in
        ffl_expiration_year = str(curr_year)[0:3] + str(ffl_expiration_year_last_num)

    else:
        # FFL expires in the next decade.. ie. the current year is 2008, but the last digit of the FFL's
        # expiration year is "3". The FFL's license couldn't have been expired already (ie 200*3), so it must
        # be expiring in 2013, 5 years from now.

        ffl_expiration_year = str((int(str(curr_year)[0:3]) + 1)) + str(ffl_expiration_year_last_num)

    return ffl_expiration_year


def calculate_expiration_date(ffl_date_code, month_code_file):

    if len(ffl_date_code) != 2:
        raise ValueError(f"ERROR: Invalid date code '{ffl_date_code}', can only have 2 characters")
    

    ffl_expiration_year_last_num, ffl_expiration_month_raw = ffl_date_code

    if not str(ffl_expiration_year_last_num).isnumeric() or not str(ffl_expiration_month_raw).isalpha():
        raise ValueError(f"ERROR: Date code {ffl_date_code} does not adhere to format!")


    month_codes = load_month_codes(month_code_file)

    ffl_expiration_month = month_codes.get(ffl_expiration_month_raw)
    ffl_expiration_year = calculate_expiration_year(int(ffl_expiration_year_last_num))

    print(f"[DEBUG] FFL expires on {ffl_expiration_month} {ffl_expiration_year} ({calculate_days_until_ffl_expiration(ffl_expiration_month, int(ffl_expiration_year))} days)")
