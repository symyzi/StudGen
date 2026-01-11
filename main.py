import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    columns = [
        "Hours_Studied",
        "Attendance",
        "Sleep_Hours",
        "Exam_Score",
        "Motivation_Level",
        "Tutoring_Sessions",
        "Family_Income"
    ]

    df = df[columns]
    df.dropna(inplace=True)

    return df

df = load_data("student_success_factors.csv")
print(df)