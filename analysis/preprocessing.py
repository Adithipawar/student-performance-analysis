# preprocessing.py
import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, skiprows=4)

    subjects = [
        "Maths", "Physics", "Principles_of_Programming",
        "Introduction_to_Electronics", "Elective_Subject",
        "English", "Indian_Constitution", "Scientific_Foundations"
    ]

    identifier_columns = ['USN', 'Name', 'Semester', 'Section']
    components = ['CIA', 'SEE', 'S-REDUCED', 'TOTAL', 'GRADE', 'REMARKS']

    new_columns = identifier_columns[:]
    for subject in subjects:
        for comp in components:
            new_columns.append(f"{subject}_{comp}")

    extra_cols = df.columns[len(new_columns):]
    new_columns.extend(extra_cols)

    df.columns = new_columns

    for subject in subjects:
        df[f"{subject}_TOTAL"] = pd.to_numeric(df[f"{subject}_TOTAL"], errors='coerce')

    return df, subjects
