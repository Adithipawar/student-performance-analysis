# --- performance_analysis.py ---
def calculate_subject_averages(df, subjects):
    averages = {}
    for subject in subjects:
        averages[subject] = df[f"{subject}_TOTAL"].mean()
    return averages

def get_top_scorers(df, subject, top_n=3):
    return df[['USN', 'Name', f"{subject}_TOTAL"]].sort_values(by=f"{subject}_TOTAL", ascending=False).head(top_n)

def get_weak_scorers(df, subject, bottom_n=3):
    return df[['USN', 'Name', f"{subject}_TOTAL"]].sort_values(by=f"{subject}_TOTAL", ascending=True).head(bottom_n)

def get_student_by_usn(df, usn):
    return df[df['USN'] == usn].squeeze()

def calculate_overall_statistics(df, subjects):
    stats = {}
    for subject in subjects:
        stats[subject] = {
            "max": df[f"{subject}_TOTAL"].max(),
            "min": df[f"{subject}_TOTAL"].min(),
            "avg": df[f"{subject}_TOTAL"].mean()
        }
    return stats
