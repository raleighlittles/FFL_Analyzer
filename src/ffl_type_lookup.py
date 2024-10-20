import csv
import pdb
import os

import helpers

# def load_ffl_types_table(ffl_types_filename) -> dict:

#     ffl_types = dict()

#     with open(ffl_types_filename, mode='r') as ffl_types_file_obj:

#         csv_reader = csv.reader(ffl_types_file_obj, skipinitialspace=True)

#         for row_idx, row_val in enumerate(csv_reader):

#             if row_idx == 0:
#                 # skip headers
#                 continue

#             ffl_types[int(row_val[0].strip())] = row_val[1].strip()

#     return ffl_types


def lookup_ffl_types(ffl_types_series):

    ffl_types_filename = "../data/ffl_types.csv"

    if not os.path.exists(ffl_types_filename):
        raise FileNotFoundError(f"Cannot find FFL types file")
    
    ffl_types_and_descr = helpers.get_csv_as_dict(ffl_types_filename, 0, 1)

    ffl_descriptions = list()

    for ffl_type in ffl_types_series:
        ffl_description = ffl_types_and_descr.get(ffl_type)
        ffl_descriptions.append(ffl_description)

    return ffl_descriptions