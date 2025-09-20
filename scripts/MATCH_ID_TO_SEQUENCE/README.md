# FASTA File Matcher

The script ```ID_sequence_match.py``` maps IDs from a CSV file to corresponding `.fasta` files located in the same directory (and its subdirectories). 
**The script can however be edited on ```line 32``` to work for other extensions**

---

## 🚀 Features
- Recursively searches for `.fasta` files in the directory of the input CSV.
- Uses fuzzy string matching to handle typos or partial matches.
- Appends the absolute path of the best-matched `.fasta` file to a new column in the CSV.
- Outputs results into a new file: `output.csv`.
- The current cutoff is ```0.6``` but can be modified.
---

## 📦 Requirements
No external dependencies in python are needed. It uses only the standard library.

---

## ⚡ Usage

```
python ID_sequence_match.py <input_csv>
```

---

## 📥 Input Format of the CSV file

**The input CSV should contain at least one column. The first column is used as the search_id for matching .fasta files.**

Example (sample.csv):

| GeneID | Description       |
|--------|-------------------|
| geneA  | Important enzyme  |
| geneB  | Transport protein |
| geneX  | Unknown           |

---

## 📥 Output Format of the CSV file

**The script creates a new file called output.csv with an additional column Fasta_Path that contains the absolute path of the matched fasta file, or "Not Found" if no match exists.**

Example (output.csv):

| GeneID | Description        | Fasta_Path                                       |
|--------|--------------------|--------------------------------------------------|
| geneA  | Important enzyme   | /home/user/project/data/geneA.fasta              |
| geneB  | Transport protein  | /home/user/project/data/subdir/geneB_sequence.fasta |
| geneX  | Unknown            | Not Found                                        |


---


