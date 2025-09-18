import os
import pandas as pd
from fuzzywuzzy import fuzz
# === CONFIGURATION ===
ids_csv_path = 'ids.csv'  # Path to your CSV with IDs
fasta_dir = 'Fasta'       # Directory containing fasta files
fastq_dir = 'Fastq'       # Directory containing fastq files
output_csv = 'match_results.csv'  # Output CSV file name

# Load IDs from CSV (assuming there's a column named 'ID')
ids_df = pd.read_csv(ids_csv_path)
ids = ids_df['ID'].astype(str).tolist()

# Get list of file names from both folders
fasta_files = os.listdir(fasta_dir)
fastq_files = os.listdir(fastq_dir)

# Function to find best match and its score in a list of filenames
def find_best_match(id_str, files):
    best_score = 0
    for file in files:
        score = fuzz.partial_ratio(id_str.lower(), file.lower())
        if score > best_score:
            best_score = score
    return (1, best_score) if best_score >= 80 else (0, 0)

# Process each ID
results = []

for id_str in ids:
    fasta_match, fasta_score = find_best_match(id_str, fasta_files)
    fastq_match, fastq_score = find_best_match(id_str, fastq_files)
    results.append({
        'ID': id_str,
        'Fasta': fasta_match,
        'Fasta percentage': fasta_score,
        'Fastq': fastq_match,
        'Fastq percentage': fastq_score
    })

# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv(output_csv, index=False)

print(f"Matching complete. Results saved to '{output_csv}'")

