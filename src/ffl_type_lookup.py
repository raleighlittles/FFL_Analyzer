import csv
import pdb
import os

import helpers

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