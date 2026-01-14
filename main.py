import parse as par

from top20 import calculate_top20_averages

df = par.load_and_prepare_data("student_success_factors.csv")
print(df)

print("Запуск анализа топ-20 студентов:")
calculate_top20_averages("student_success_factors.csv")
