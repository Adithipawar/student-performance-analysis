# --- visualizations.py ---
import matplotlib.pyplot as plt
import seaborn as sns

def plot_average_marks(df, subjects):
    avg_marks = [df[f"{sub}_TOTAL"].mean() for sub in subjects]
    plt.figure(figsize=(12, 6))
    sns.barplot(x=subjects, y=avg_marks, palette='viridis')
    plt.title("📊 Average Marks per Subject")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_heatmap(df, subjects):
    heatmap_data = df[[f"{sub}_TOTAL" for sub in subjects]]
    heatmap_data.index = df["USN"]
    plt.figure(figsize=(14, 10))
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.5)
    plt.title("🔥 Student-wise Subject Performance (Total Marks)")
    plt.xlabel("Subjects")
    plt.ylabel("USN")
    plt.tight_layout()
    plt.show()

def plot_individual_student(df, subjects, usn):
    student = df[df["USN"] == usn]
    if not student.empty:
        marks = [student[f"{sub}_TOTAL"].values[0] for sub in subjects]
        plt.figure(figsize=(10, 6))
        plt.plot(subjects, marks, marker='o', label=usn)
        plt.title(f"📈 Performance of {usn}")
        plt.ylabel("Total Marks")
        plt.ylim(0, 100)
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"USN {usn} not found.")
