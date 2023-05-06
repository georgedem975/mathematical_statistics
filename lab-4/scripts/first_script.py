import pandas as pd
import numpy as np
from scipy.stats import kstest, uniform, chisquare, chi2

# Читаем данные из файла
data = pd.read_csv('mobile_phones.csv')

# Стандартизация данных (нужна для того чтобы получить правильные данные)
min_value = data['battery_power'].min()
max_value = data['battery_power'].max()
data['uniform'] = (data['battery_power'] - min_value) / (max_value - min_value)

# Проверка гипотезы о равномерности распределения
alpha = 0.05
stat, p = kstest(data['uniform'], uniform.cdf)
print('Колмогоров-Смирнов')
if p > alpha:
    print('H0 верна')
else:
    print('H1 верна')

# Разбиение диапазона значений на интервалы
k = 10
bins = np.linspace(data['battery_power'].min(), data['battery_power'].max(), k+1)
labels = np.arange(1, k+1)
data['interval'] = pd.cut(data['battery_power'], bins=bins, labels=labels, include_lowest=True)

# Вычисление наблюдаемых частот
observed_freq = data.groupby('interval').size()

# Вычисление ожидаемых частот при равномерном распределении
total = len(data)
expected_freq = total / k

# Проверка гипотезы о равномерности распределения
statistic = sum((observed_freq - expected_freq) ** 2 / expected_freq)
p_value = 1 - chi2.cdf(statistic, k - 1)

# Вывод результатов теста
print('хи-квадрат')
alpha = 0.05
if p_value > alpha:
    print('H0 верна')
else:
    print('H1 верна')