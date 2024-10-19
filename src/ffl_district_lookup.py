import csv
import pdb

def load_districts_table(districts_table_filename) -> dict:

    district_codes = dict()

    with open(districts_table_filename, mode='r') as districts_table_file_obj:

        csv_reader = csv.reader(districts_table_file_obj, skipinitialspace=True)

        for row_idx, row_val in enumerate(csv_reader):

            if row_idx == 0:
                # skip headers
                continue

            site_hq = f"{row_val[0]}"

            if row_val[1] != "N/A":
                site_hq += f", {row_val[1]}"

            district_codes_for_site = row_val[2].split(",")

            for district_code in district_codes_for_site:
                district_codes[int(district_code.strip())] = site_hq

    return district_codes

    
def lookup_district_names_from_code(district_codes):

    district_dict = load_districts_table("../data/irs_districts.csv")

    district_names = list()

    for district_code in district_codes:

        district_hq = district_dict.get(district_code)
        district_names.append(district_hq)

    return district_names