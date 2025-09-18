import pandas as pd
from rapidfuzz import fuzz, process
from openpyxl import Workbook

# === CONFIG ===
csv_file = "input.csv"       # input CSV filename
col_a = "ColumnA"            # name of first column
col_b = "ColumnB"            # name of second column
output_file = "output.xlsx"  # output Excel filename

# === STEP 1: Load Data ===
df = pd.read_csv(csv_file)

# Ensure the chosen columns exist
if col_a not in df.columns or col_b not in df.columns:
    raise ValueError(f"CSV must contain '{col_a}' and '{col_b}'")

values_a = df[col_a].dropna().astype(str).tolist()
values_b = df[col_b].dropna().astype(str).tolist()

# === STEP 2: Compare and calculate similarity ===
matches = []
unmatched = []

for val_a in values_a:
    # Find best match in ColumnB
    best_match, score, _ = process.extractOne(val_a, values_b, scorer=fuzz.ratio)

    if score > 50:
        matches.append([val_a, best_match, score])
    else:
        unmatched.append([val_a, col_a])

# Now check values in ColumnB that were not matched
for val_b in values_b:
    # Find best match in ColumnA
    best_match, score, _ = process.extractOne(val_b, values_a, scorer=fuzz.ratio)

    if score <= 50:
        unmatched.append([val_b, col_b])

# === STEP 3: Write to Excel ===
wb = Workbook()

# Sheet 1: Matches
ws1 = wb.active
ws1.title = "Matches"
ws1.append(["ColumnA Value", "ColumnB Match", "Similarity (%)"])
for row in matches:
    ws1.append(row)

# Sheet 2: Unmatched
ws2 = wb.create_sheet("Unmatched")
ws2.append(["Unmatched Value", "Original Column"])
for row in unmatched:
    ws2.append(row)

# Save file
wb.save(output_file)

print(f"✅ Processing complete! Results saved in '{output_file}'")

