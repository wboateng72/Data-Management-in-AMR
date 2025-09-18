## 🔍 Script Function and Usage

The script performs the following tasks:  
- 📥 Reads a list of IDs from a CSV file (`ids.csv`).  
- 📂 Scans both `Fasta` and `Fastq` directories for available files.  
- 🤖 Uses fuzzy matching (`fuzzywuzzy`) to check whether each ID is represented in the file names (allowing for minor naming inconsistencies).  
- 📊 Records whether a match was found and the percentage similarity score.  
- 💾 Exports the results into a summary CSV (`match_results.csv`).  

**Example Output (`match_results.csv`):**

| ID      | Fasta | Fasta percentage | Fastq | Fastq percentage |
|---------|-------|------------------|-------|------------------|
| Sample1 | 1     | 95               | 1     | 98               |
| Sample2 | 0     | 0                | 1     | 87               |

### ⚡️ How to Use

Clone the repository and move into it:
```bash
git clone https://github.com/your-username/amr-data-management.git
cd amr-data-management
```

Set up a Python virtual environment
```
python3 -m venv env
source env/bin/activate
```

Make sure you have Python 3.7 or higher installed, then run:
```
pip install pandas fuzzywuzzy python-Levenshtein
```

Edit the parameters at the top of the script if needed:

ids_csv_path = 'ids.csv'         # Path to your CSV with IDs
fasta_dir = 'Fasta'              # Directory containing fasta files
fastq_dir = 'Fastq'              # Directory containing fastq files
output_csv = 'match_results.csv' # Output CSV file name

Run the script:
```
python match_ids.py
```

Check the results

A new file named match_results.csv will be created with the matching results.


🤝 Contributions

Contributions are welcome!
Feel free to open an issue or submit a pull request.