import pandas
import argparse
import os

def csv_to_markdown(csv_file):

    with open(csv_file + ".md", mode="w", encoding="utf-8") as output_md_file:
        pandas.read_csv(csv_file, sep=",", quotechar='"', skipinitialspace=True).to_markdown(buf=output_md_file, tablefmt="github")
    

if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-d", "--csv-dir", type=str, required=True, help="The directory to look for CSV files")

    argparse_args = argparse_parser.parse_args()

    if not os.path.exists(argparse_args.csv_dir):
        raise FileNotFoundError(f"ERROR: Directory '{argparse_args.csv_dir} does not exist!")
    
    num_files_processed = 0
        
    for candidate_file in os.listdir(argparse_args.csv_dir):

        candidate_filename = os.fsdecode(candidate_file)

        if candidate_filename.endswith(".csv"):

            print(f"[DEBUG] Converting CSV file {candidate_file} (size={os.path.getsize(candidate_file)} bytes) to Markdown")
            csv_to_markdown(candidate_filename)
            num_files_processed += 1


    print(f"[DEBUG] Finished processing {num_files_processed} CSV files from {argparse_args.csv_dir}")
