# =============================================================================
# convert-excel-to-csv.py
# PythonMuse AI Accounting Framework
#
# Converts Excel files (.xlsx) to clean CSV format.
# Handles multiple sheets, cleans column names, and preserves data types.
# =============================================================================

import pandas as pd
import os
import sys

def clean_column_name(name):
    """
    Standardize a column name for consistency.
    - Strip leading/trailing whitespace
    - Convert to lowercase
    - Replace spaces with underscores
    - Remove special characters
    """
    clean = str(name).strip().lower()
    clean = clean.replace(" ", "_")
    clean = clean.replace("(", "").replace(")", "")
    clean = clean.replace("/", "_")
    clean = clean.replace("-", "_")
    return clean


def convert_excel_to_csv(excel_path, output_dir=None):
    """
    Convert an Excel file to CSV format.

    - If the workbook has one sheet, creates a single CSV
    - If it has multiple sheets, creates one CSV per sheet
    - Cleans column names for consistency
    - Preserves dates and numbers
    """

    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(excel_path)

    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(excel_path))[0]

    # Read all sheet names from the workbook
    xlsx = pd.ExcelFile(excel_path, engine="openpyxl")
    sheet_names = xlsx.sheet_names

    print(f"File: {excel_path}")
    print(f"Sheets found: {len(sheet_names)} -- {sheet_names}")
    print()

    files_created = []

    for sheet_name in sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xlsx, sheet_name=sheet_name)

        # Clean column names
        df.columns = [clean_column_name(col) for col in df.columns]

        # Remove completely empty rows (common in Excel exports)
        df = df.dropna(how="all")

        # Build the output filename
        if len(sheet_names) == 1:
            csv_filename = f"{base_name}.csv"
        else:
            # Include sheet name for multi-sheet workbooks
            safe_sheet = sheet_name.strip().lower().replace(" ", "_")
            csv_filename = f"{base_name}_{safe_sheet}.csv"

        csv_path = os.path.join(output_dir, csv_filename)

        # Save to CSV with UTF-8 encoding
        df.to_csv(csv_path, index=False, encoding="utf-8")

        files_created.append(csv_path)
        print(f"  Created: {csv_path}")
        print(f"    Rows: {len(df)} | Columns: {len(df.columns)}")
        print(f"    Columns: {list(df.columns)}")
        print()

    return files_created


# =============================================================================
# Example Usage
# =============================================================================
if __name__ == "__main__":
    # You can run this script from the command line:
    #   python convert-excel-to-csv.py path/to/file.xlsx output_directory/
    #
    # Or modify the paths below and run directly.

    if len(sys.argv) >= 2:
        excel_file = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) >= 3 else None
        convert_excel_to_csv(excel_file, output)
    else:
        print("Usage: python convert-excel-to-csv.py <excel_file> [output_directory]")
        print()
        print("Example:")
        print("  python convert-excel-to-csv.py data/raw/report.xlsx data/processed/")
