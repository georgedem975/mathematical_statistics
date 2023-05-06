import pandas as pd
from scipy.stats import chi2_contingency

# Читаем данные из файла
data = pd.read_csv('mobile_phones.csv')

# Создаем таблицу сопряженности
contingency_table = pd.crosstab(data['three_g'], data['wifi'])

# Применяем критерий хи-квадрат
chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

# Выводим результаты
if p_value < 0.05:
    print("Гипотеза H0 отвергается в пользу гипотезы H1.")
    print("Количество телефонов с поддержкой 3G больше количества телефонов с Wi-Fi.")
else:
    print("Гипотеза H0 не отвергается.")