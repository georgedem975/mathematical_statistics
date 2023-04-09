import numpy as np
from scipy.stats import f

n = 25
m = 25
alpha = 0.05
num_trials = 1000

# Генерируем выборки X и Y
X = np.random.normal(loc=0, scale=1, size=n)
Y = np.random.normal(loc=0.5, scale=1.5, size=m)

# Вычисляем выборочные смещенные дисперсии
var_X = np.var(X, ddof=1)
var_Y = np.var(Y, ddof=1)

# Вычисляем статистику для параметра tau
tau = (n * (m-1) * var_X) / (m * (n-1) * var_Y)

# Вычисляем квантили распределения Фишера
q1 = f.ppf(1 - alpha/2, n-1, m-1)
q2 = f.ppf(alpha/2, n-1, m-1)

# Вычисляем доверительный интервал
ci_low = tau / q1
ci_high = tau / q2

# Подсчитываем, сколько раз доверительный интервал покрывает истинное значение параметра
num_covered = 0
for i in range(num_trials):
    X = np.random.normal(loc=0, scale=1, size=n)
    Y = np.random.normal(loc=0.5, scale=1.5, size=m)
    var_X = np.var(X, ddof=1)
    var_Y = np.var(Y, ddof=1)
    tau = (n * (m-1) * var_X) / (m * (n-1) * var_Y)
    q1 = f.ppf(1 - alpha/2, n-1, m-1)
    q2 = f.ppf(alpha/2, n-1, m-1)
    ci_low = tau / q1
    ci_high = tau / q2
    if ci_low <= 1 <= ci_high:
        num_covered += 1

# Выводим результаты
coverage_rate = num_covered / num_trials
print(f'Для выборки объема {n} доверительный интервал покрывает реальное значение параметра в {coverage_rate:.3f} случаях')


# Генерируем выборки
n = 10000
m = 10000

coverage = 0
for i in range(num_trials):
    X = np.random.normal(loc=0, scale=1, size=n)
    Y = np.random.normal(loc=0, scale=1, size=m)

    # Считаем выборочные дисперсии
    var_X = np.var(X, ddof=1)
    var_Y = np.var(Y, ddof=1)

    # Считаем статистику и квантили распределения Фишера
    statistic = (n * (m - 1) * var_X) / (m * (n - 1) * var_Y)
    q1 = f.ppf(0.025, n-1, m-1)
    q2 = f.ppf(0.975, n-1, m-1)

    # Считаем доверительный интервал
    ci = [statistic * (1/q2), statistic * (1/q1)]

    # Проверяем, попадает ли истинное значение в доверительный интервал
    if ci[0] <= 1 <= ci[1]:
        coverage += 1

print(f'Для выборки объема {n} доверительный интервал покрывает реальное значение параметра в {coverage:.3f} случаях')