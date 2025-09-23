# 🧬 FASTA File Collector

This repository contains a simple **Bash script** for collecting specified files from different locations and copying them into a single destination folder.  
It is especially useful in **bioinformatics pipelines**, where multiple assemblies or sequence files need to be consolidated into one place before downstream analysis.

---

## 📂 Script Function

- Creates a folder called `assembly` (It can be replaced with any folder name you choose).
- Copies a predefined list of `.fasta` files into the folder. Modify by providing path to all your files
- Checks whether each file exists before copying.
- Provides informative messages:
  - ✅ File successfully copied
  - ⚠️ File not found

---

## ⚙️ Usage

1. **Clone this repository** (or copy the script into your project):

2. Make the script executable (**take note of script name**):
```
chmod +x file_transfer.sh
```

3. Edit the script:
- Open copy_fasta.sh in a text editor.
- Update the files array with the full paths to your FASTA files.
- Change the folder variable if you want a different destination.

4. Run the script:
```
./file_transfer.sh
```

👨‍💻 Author

Created by **William Boateng**