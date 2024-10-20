import csv


def get_csv_as_dict(csv_filename, key_column_idx, value_column_idx):

    csv_as_dict = dict()

    with open(csv_filename, mode='r') as csv_file_obj:

        csv_reader = csv.reader(csv_file_obj, skipinitialspace=True)

        for row_idx, row_val in enumerate(csv_reader):

            # Skip headers
            if row_idx == 0:
                continue

            csv_as_dict[int(row_val[key_column_idx].strip())] = row_val[value_column_idx].strip()

    return csv_as_dict