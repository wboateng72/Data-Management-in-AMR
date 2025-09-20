import os
import sys
import csv
import difflib

def find_best_fasta_match(search_id, fasta_files):
    """
    Find the best matching fasta file for a given ID (case-insensitive) using fuzzy matching.
    Returns the absolute path if found, otherwise 'Not Found'.
    """
    if not fasta_files:
        return "Not Found"

    # Work on lowercase basenames for comparison, but preserve full paths
    basenames = [os.path.basename(f).lower() for f in fasta_files]
    matches = difflib.get_close_matches(search_id.lower(), basenames, n=1, cutoff=0.6)

    if matches:
        # Get the original full path of the best match
        match_idx = basenames.index(matches[0])
        return os.path.abspath(fasta_files[match_idx])

    return "Not Found"

def collect_fasta_files(root_dir):
    """
    Recursively collect all .fasta files from the root directory and subdirectories.
    """
    fasta_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.lower().endswith(".fasta"):  # case-insensitive extension
                fasta_files.append(os.path.join(dirpath, file))
    return fasta_files

def process_csv(input_csv):
    """
    Reads the input CSV, finds best matching fasta files for each ID,
    and writes results to a new CSV file.
    """
    root_dir = os.path.dirname(os.path.abspath(input_csv))
    fasta_files = collect_fasta_files(root_dir)

    output_csv = os.path.join(root_dir, "output.csv")
    
    with open(input_csv, "r", newline="") as infile, open(output_csv, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        header.append("Fasta_Path")
        writer.writerow(header)

        for row in reader:
            if not row:  # skip empty rows
                continue
            search_id = row[0].strip()
            best_match = find_best_fasta_match(search_id, fasta_files)
            row.append(best_match)
            writer.writerow(row)

    print(f"Processing complete. Output saved to {output_csv}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_csv>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    process_csv(input_csv)
