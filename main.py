import pandas as pd

def load_and_prepare_data(path: str) -> pd.DataFrame:

    # Загрузка данных
    df = pd.read_csv(path)

    # Отбор нужных столбцов
    selected_columns = {
        "Hours_Studied": "hours_studied",
        "Attendance": "attendance",
        "Sleep_Hours": "sleep_hours",
        "Exam_Score": "exam_score",
        "Motivation_Level": "motivation",
        "Tutoring_Sessions": "tutoring_sessions",
        "Family_Income": "family_income"
    }

    df = df[list(selected_columns.keys())]
    df.rename(columns=selected_columns, inplace=True)

    # Проверка пропусков
    missing = df.isnull().sum()
    print("Пропущенные значения:\n", missing)

    # Удаление строк с пропущенными ключевыми значениями
    df.dropna(subset=["exam_score"], inplace=True)

    # Заполнение пропусков
    numeric_cols = [
        "hours_studied",
        "attendance",
        "sleep_hours",
        "tutoring_sessions"
    ]

    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)

    # Кодирование категориальных признаков
    motivation_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    income_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    df["motivation"] = df["motivation"].map(motivation_map)
    df["family_income"] = df["family_income"].map(income_map)

    # Приведение типов
    df = df.astype({
        "hours_studied": float,
        "attendance": float,
        "sleep_hours": float,
        "exam_score": float,
        "tutoring_sessions": int,
        "motivation": int,
        "family_income": int
    })

    # Валидация значений
    df = df[
        (df["attendance"] >= 0) & (df["attendance"] <= 100) &
        (df["sleep_hours"] >= 0) &
        (df["exam_score"] >= 0) & (df["exam_score"] <= 100)
    ]

    return df


df = load_and_prepare_data("student_success_factors.csv")
print(df)