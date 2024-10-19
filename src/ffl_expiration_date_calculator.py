import datetime
import csv
import time

def load_month_codes(month_code_filename) -> dict:

    month_codes = dict()

    with open(month_code_filename, mode='r') as month_code_csv_file_obj:
        csv_reader = csv.reader(month_code_csv_file_obj)
        
        for row_idx, row_val in enumerate(csv_reader):

            # skip headers
            if row_idx == 0:
                continue

            month_codes[row_val[0].strip()] = row_val[1].strip()

    return month_codes


def calculate_expiration_year(ffl_expiration_year_last_num) -> int:

    curr_year = datetime.datetime.now().year

    ffl_expiration_year = 0
    last_digit_of_curr_year = int(str(curr_year)[-1])

    if (last_digit_of_curr_year < ffl_expiration_year_last_num):
        # The FFL expires in the same decade that we're in
        ffl_expiration_year = str(curr_year)[0:3] + str(ffl_expiration_year_last_num)

    elif (last_digit_of_curr_year > ffl_expiration_year_last_num):
        # FFL expires in the next decade.. ie. the current year is 2008, but the last digit of the FFL's
        # expiration year is "3". The FFL's license couldn't have been expired already (ie 200*3), so it must
        # be expiring in 2013, 5 years from now.
        ffl_expiration_year = str((int(str(curr_year)[0:3]) + 1)) + str(ffl_expiration_year_last_num)

    else:
        # We've checked the greater-than case, and the less-than case, the only case remaining is the equals
        # FFL licenses last less than 10 years, so if the last digit of their expiration year is the same 
        # as the last digit of our current year, the FFL must be expiring THIS year.
        ffl_expiration_year = curr_year

    return ffl_expiration_year


def calculate_expiration_date(ffl_date_code, month_code_file):

    if len(ffl_date_code) != 2:
        raise ValueError(f"ERROR: Invalid date code '{ffl_date_code}', can only have 2 characters")
    
    ffl_expiration_year_last_num, ffl_expiration_month_raw = ffl_date_code

    if not str(ffl_expiration_year_last_num).isnumeric() or not str(ffl_expiration_month_raw).isalpha():
        raise ValueError(f"ERROR: Date code {ffl_date_code} does not adhere to format!")


    month_codes_dict = load_month_codes(month_code_file)

    ffl_expiration_month = month_codes_dict.get(ffl_expiration_month_raw)
    ffl_expiration_year = calculate_expiration_year(int(ffl_expiration_year_last_num))

    #print(f"[DEBUG] FFL expires on {ffl_expiration_month} {ffl_expiration_year}")

    ffl_expiration_month_as_int = int(time.strptime(ffl_expiration_month, "%B").tm_mon)

    ffl_expiration_datetime = datetime.datetime(year=int(ffl_expiration_year), month=ffl_expiration_month_as_int, day=1)

    return ffl_expiration_datetime

def calculate_expiration_dates_and_days_remaining(expiration_date_code_series):

    month_code_file = "../data/date_letter_codes.csv"

    expiration_dates_formatted = list()
    expiration_days_until = list()

    curr_timestamp = datetime.datetime.now()

    for expiry_date in expiration_date_code_series:

        expiration_date_datetime = calculate_expiration_date(expiry_date, month_code_file)

        expiration_days_until.append((expiration_date_datetime - curr_timestamp).days)

        expiration_dates_formatted.append(expiration_date_datetime.strftime("%Y-%m-%d"))

    if len(expiration_days_until) != len(expiration_dates_formatted):
        raise ValueError(f"Error parsing dates!")

    return (expiration_dates_formatted, expiration_days_until)