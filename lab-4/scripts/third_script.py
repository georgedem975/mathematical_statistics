import pandas as pd
from scipy.stats import chi2_contingency

# Читаем данные из файла
data = pd.read_csv('mobile_phones.csv')

# Создание двух категориальных переменных: «Цена» и «Объем оперативной памяти».
price_category = pd.cut(data['price_range'], bins=[0, 1, 2, 3, 4], labels=['0-1', '1-2', '2-3', '3-4'])
ram_category = pd.cut(data['ram'], bins=[0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000],
                      labels=['0-2GB', '2-4GB', '4-6GB', '6-8GB', '8-10GB', '10-12GB', '12-14GB', '14-16GB', '16-18GB', '18-20GB'])
# Создание таблицы сопряженности для двух категориальных переменных.
contingency_table = pd.crosstab(price_category, ram_category)

# Применение критерия хи-квадрат для проверки независимости двух категориальных переменных.
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Оценка p-значения.
alpha = 0.05
if p_value < alpha:
    print('Отвергаем H0, принимаем H1')
else:
    print('Не получилось отвергнуть H0')