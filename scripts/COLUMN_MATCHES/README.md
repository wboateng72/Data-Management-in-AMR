## ⚙️ Functionality

This script automates the comparison of two columns in a CSV file to identify **similar** and **unmatched** values:

1. **Load Data** – Reads a CSV file and extracts values from two specified columns.  

2. **Fuzzy Matching** – Uses `rapidfuzz` to calculate similarity scores between entries in both columns.  
   - Matches above a threshold (default: **50%**) are recorded.  
   - Unmatched values from both columns are flagged.  

3. **Export Results** – Saves results to an Excel file with two sheets:  
   - **Matches** → side-by-side matches with similarity percentages.  
   - **Unmatched** → values that did not meet the similarity threshold.  

✅ Output is an easy-to-read **Excel report** for quick inspection and further analysis.



## 🔧 Environment Setup & Installation
### Create and Activate a Virtual Environment

```
python -m venv venv
source venv/bin/activate 
```

### Install Dependencies

```
pip install pandas rapidfuzz openpyxl
```

Edit the parameters at the top of the script if needed:

csv_file = "input.csv"       # Path to your input CSV file

col_a = "ColumnA"            # Name of the first column to compare

col_b = "ColumnB"            # Name of the second column to compare

output_file = "output.xlsx"  # Name of the Excel file for results
