#!/bin/bash
folder="assembly"
# Make sure the destination folder exists
mkdir -p "$folder"

# List of fasta file paths (paste your full list here)
files=(
/hpc/Fasta/LH001.fasta
/hpc/Fasta/LH101.fasta
/hpc/Fasta/LH1001.fasta
/hpc/Fasta/SL01901.fasta
)

# Copy each file into folder
for f in "${files[@]}"; do
    if [[ -f "$f" ]]; then
        cp "$f" "$folder"
        echo "Copied: $f"
    else
        echo "File not found: $f"
    fi
done

echo "✅ All available files copied to $folder"

