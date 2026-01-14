import parse as par
import correlation as cor
from top20 import calculate_top20_averages
import patterns as pat

df = par.load_and_prepare_data("student_success_factors.csv")
print(df)

print("Запуск анализа топ-20 студентов:")
calculate_top20_averages(df)
cor.plot_correlations(df)
pat.patterns(df)


