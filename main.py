import parse as par
import correlation as cor
from top20 import calculate_top20_averages
import patterns as pat

df = par.load_and_prepare_data("student_success_factors.csv")
print(df)
print("\nЗапуск анализа топ-20 студентов: \n")
calculate_top20_averages(df)
print("\nПостроение корреляций: \n")
cor.plot_correlations(df)
print("\nПоиск паттернов: \n")
pat.patterns(df)


