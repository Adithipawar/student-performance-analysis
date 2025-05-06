import pandas as pd

def load_and_clean_data(file):
    # Load the CSV normally — inspect for correct starting row
    df = pd.read_csv(file)

    # Drop any unnamed columns (usually extra empty ones)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]

    # Standardize column names
    df.columns = df.columns.str.strip().str.upper()

    # Rename common columns (flexible mapping)
    rename_map = {}
    for col in df.columns:
        if 'USN' in col:
            rename_map[col] = 'USN'
        elif 'NAME' in col:
            rename_map[col] = 'NAME'
        elif 'TOTAL' in col:
            rename_map[col] = 'TOTAL'
        elif 'RESULT' in col:
            rename_map[col] = 'RESULT'
        elif 'SGPA' in col:
            rename_map[col] = 'SGPA'
        elif 'CGPA' in col:
            rename_map[col] = 'CGPA'

    df.rename(columns=rename_map, inplace=True)

    # Identify subject columns (exclude known non-subject columns)
    non_subject_cols = {'USN', 'NAME', 'TOTAL', 'RESULT', 'SGPA', 'CGPA'}
    subject_cols = [col for col in df.columns if col not in non_subject_cols]

    return df, subject_cols
