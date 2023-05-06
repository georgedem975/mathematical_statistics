### Лабораторная работа №4 (Вариант №2)

---

Для каждого вопроса требуется формализовать задачу и проверить статистическую гипотезу двумя критериями, если не сказано иное.

В файле mobile_phones.cvs ([исходник отсюда]()) представлены данные о мобильных телефонах.

1. Разумно ли считать, что емкость аккумулятора распределена равномерно?

Формализуем задачу:

H0: Емкость аккумулятора распределена равномерно.
H1: Емкость аккумулятора не распределена равномерно.

Для проверки этой гипотезы мы можем использовать два критерия: критерий хи-квадрата и критерий Колмогорова-Смирнова

Надо заметить что в критерии Колмогорова-Смирнова, надо использовать стандартизированные данные, так как ```uniform.cdf``` должна принимать значения в интервале ```[0, 1]```, а в качестве аргументов ей передаются фактические значения аккумуляторов.

```python
import pandas as pd
import numpy as np
from scipy.stats import kstest, uniform, chisquare, chi2

data = pd.read_csv('mobile_phones.csv')

min_value = data['battery_power'].min()
max_value = data['battery_power'].max()
data['uniform'] = (data['battery_power'] - min_value) / (max_value - min_value)

alpha = 0.05
stat, p = kstest(data['uniform'], uniform.cdf)
print('Колмогоров-Смирнов')
if p > alpha:
    print('H0 верна')
else:
    print('H1 верна')

k = 10
bins = np.linspace(data['battery_power'].min(), data['battery_power'].max(), k+1)
labels = np.arange(1, k+1)
data['interval'] = pd.cut(data['battery_power'], bins=bins, labels=labels, include_lowest=True)

observed_freq = data.groupby('interval').size()

total = len(data)
expected_freq = total / k

statistic = sum((observed_freq - expected_freq) ** 2 / expected_freq)
p_value = 1 - chi2.cdf(statistic, k - 1)

print('хи-квадрат')
alpha = 0.05
if p_value > alpha:
    print('H0 верна')
else:
    print('H1 верна')
```

вывод:
```
Колмогоров-Смирнов
H0 верна
хи-квадрат
H0 верна
```

Оба критерия, Колмогорова-Смирнова и хи-квадрат, дают вывод о том, что гипотеза ```H0``` о равномерности распределения емкости аккумулятора в мобильных телефонах верна на уровне значимости ```0.05```. Это означает, что нет достаточных доказательств в данных, чтобы отвергнуть гипотезу о равномерном распределении.

2. Верно ли, что телефонов с поддержкой 3G больше моделей с Wi-Fi? А разнится ли количество телефонов с touch screen от моделей с двумя сим-картами? На каждый вопрос по тесту.

Формализуем задачу:

H0: Количество телефонов с поддержкой 3G не отличается от количества телефонов с Wi-Fi.
H1: Количество телефонов с поддержкой 3G больше количества телефонов с Wi-Fi.

```python
import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_csv('mobile_phones.csv')

contingency_table = pd.crosstab(data['three_g'], data['wifi'])

chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

if p_value < 0.05:
    print("Гипотеза H0 отвергается в пользу гипотезы H1.")
    print("Количество телефонов с поддержкой 3G больше количества телефонов с Wi-Fi.")
else:
    print("Гипотеза H0 не отвергается.")
```

вывод:
```
Гипотеза H0 не отвергается.
```

Формализуем задачу:

H0: Количество телефонов с touch screen не отличается от количества телефонов с двумя сим-картами.
H1: Количество телефонов с touch screen отличается от количества телефонов с двумя сим-картами.

```python
import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_csv('mobile_phones.csv')

contingency_table = pd.crosstab(data['touch_screen'], data['dual_sim'])

chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

if p_value < 0.05:
    print("Гипотеза H0 отвергается в пользу гипотезы H1.")
    print("Количество телефонов с touch screen отличается от количества телефонов с двумя сим-картами.")
else:
    print("Гипотеза H0 не отвергается.")
```

вывод:
```
Гипотеза H0 не отвергается.
```

3. Есть подозрение, что цена зависит от объема оперативной памяти. Проверите данное утверждение.

Формализуем задачу:

H0: Цена мобильных телефонов не зависит от объема оперативной памяти.
H1: Цена мобильных телефонов зависит от объема оперативной памяти.

Хочу так же заметить что результат данного кода может меняться в зависимотсти от выбранных значений интервалов.

```python
import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_csv('mobile_phones.csv')

price_category = pd.cut(data['price_range'], bins=[0, 1, 2, 3, 4], labels=['0-1', '1-2', '2-3', '3-4'])
ram_category = pd.cut(data['ram'], bins=[0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000],
                      labels=['0-2GB', '2-4GB', '4-6GB', '6-8GB', '8-10GB', '10-12GB', '12-14GB', '14-16GB', '16-18GB', '18-20GB'])

contingency_table = pd.crosstab(price_category, ram_category)

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

alpha = 0.05
if p_value < alpha:
    print('Отвергаем H0, принимаем H1')
else:
    print('Не получилось отвергнуть H0')
```

вывод:
```
Отвергаем H0, принимаем H1
```