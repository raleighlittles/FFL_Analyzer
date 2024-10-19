import csv
import argparse

with open("country_region.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=",", skipinitialspace=True)

    for i, line in enumerate(reader):

        if i == 0:
            # skip header row
            continue

        num_count = len(line[-1].split(","))
        print("Count ", num_count)