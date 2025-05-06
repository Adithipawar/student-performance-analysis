import pandas as pd

def load_and_clean_data(file):
    df = pd.read_csv(file)

    # Automatically rename duplicate columns to make them unique
    df.columns = pd.io.parsers.ParserBase({'names': df.columns})._maybe_dedup_names(df.columns)

    # Example: ['TOTAL', 'TOTAL_1', 'TOTAL_2', ...] if multiple 'TOTAL' columns exist

    # Clean column names: strip spaces, upper case
    df.columns = df.columns.str.strip().str.upper()

    # Optional: Display the column names (debugging)
    print(f"[DEBUG] Columns after renaming: {df.columns.tolist()}")

    # Example: Assuming USN and NAME are first two columns
    subject_columns = df.columns[2:-2]  # remove USN, NAME, SGPA, CGPA (adjust as needed)
    return df, subject_columns
