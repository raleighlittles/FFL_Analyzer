import csv
import os

import helpers

# def load_country_regions(region_code_file):

#     region_codes = dict()

#     with open(region_code_file, mode='r') as month_code_csv_file_obj:
#         csv_reader = csv.reader(month_code_csv_file_obj)
        
#         for row_idx, row_val in enumerate(csv_reader):

#             # skip headers
#             if row_idx == 0:
#                 continue

#             region_codes[int(row_val[0].strip())] = row_val[1].strip()

#     return region_codes

def calculate_country_region(region_series):

    country_regions_file = "../data/country_regions.csv"

    if not os.path.exists(country_regions_file):
        raise FileNotFoundError(f"Cannot region regions file '{country_regions_file}'")

    country_regions_dict = helpers.get_csv_as_dict("../data/country_regions.csv", 0, 1)

    region_names = list()
    
    for raw_region_code in region_series:
        region_name = country_regions_dict.get(raw_region_code)
        region_names.append(region_name)

    return region_names