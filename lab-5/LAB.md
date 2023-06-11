### Лабораторная работа №5

--- 

Задание представлено в 4 вариантах. Для каждого варианта требуется построить линейную модель, вычислить оценки коэффициентов модели и остаточной дисперсии, построить для них доверительные интервалы, вычислить коэффициент детерминации, проверить указанные в условии гипотезы с помощью построенной линейной модели.

Указание: из встроенных функций разрешается пользоваться квантильными функциями и средствами для квадратичной оптимизации (иными словами, готовую обертку для построения линейной модели не использовать)

---

Условие:

Вариант 3. В файле MEN_SHOES_.csv приведены данные о мужской обуви.

1. Постройте линейную модель, где в качестве независимых переменных выступают количество проданных экземпляров и цена (вместе со свободным коэффициентом), зависимой – рейтинг.

2. Проверьте следующие подозрения:
    + Чем больше продажи, тем больше рейтинг
    + Рейтинг за зависит от цены
    + Рейтинг зависит и от цены, и от количества проданных экземпляров


---

Решение: 

Подключим нужные библиотеки:

```python
import pandas as pd
import numpy as np
from scipy import stats
```

Далее, считаемм данные с файла:

```python 
data = pd.read_csv('path')
```

Выделим независимые и зависимые переменные:

```python
X = data[['How_Many_Sold', 'Current_Price']]
y = data['RATING']
```

Преобразуем столбцы в нужный формат:

```python
X['How_Many_Sold'] = X['How_Many_Sold'].str.replace(',', '').astype(float)
X['Current_Price'] = X['Current_Price'].str.replace('₹', '').str.replace(',', '').astype(float)
X = X.replace([np.inf, -np.inf], np.nan).fillna(0)
```

Добавим столбец с единичными значениями для свободного коэффициента:

```python
X['intercept'] = 1
```

Решим линейную модель методом наименьших квадратов:

```python
coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
```

Выдодим результаты:

```python
print('Коэффициенты модели:')
print('Intercept:', coefficients[2])
print('How_Many_Sold:', coefficients[0])
print('Current_Price:', coefficients[1])
```

Находим остаточную дисперсию:

```python
residuals = y - X.dot(coefficients)

residual_variance = np.var(residuals, ddof=X.shape[1])

print('Остаточная дисперсия:', residual_variance)
```

Вычислим стандартные ошибоки коэффициентов модели:

```python
X_transpose_X_inverse = np.linalg.inv(X.transpose().dot(X))

standard_errors = np.sqrt(np.diagonal(residual_variance * X_transpose_X_inverse))
```

Построим доверительные интервалы для коэффициентов модели:

```python
confidence_interval = 1.96 * standard_errors

lower_bounds = coefficients - confidence_interval

upper_bounds = coefficients + confidence_interval

print('Доверительные интервалы для коэффициентов модели:')
print('Intercept:', lower_bounds[2], '-', upper_bounds[2])
print('How_Many_Sold:', lower_bounds[0], '-', upper_bounds[0])
print('Current_Price:', lower_bounds[1], '-', upper_bounds[1])
```

Вычислим коэффициент детерминации:

```python
total_sum_of_squares = np.sum((y - np.mean(y)) ** 2)

explained_sum_of_squares = np.sum((X.dot(coefficients) - np.mean(y)) ** 2)

r_squared = explained_sum_of_squares / total_sum_of_squares

print('Коэффициент детерминации:', r_squared)
```

Проверим гипотезы:
```python
_, p_value_first = stats.ttest_ind(X['How_Many_Sold'], y)

_, p_value_second = stats.ttest_ind(X['Current_Price'], y)

if p_value_first < 0.05:
    print('Гипотеза "Чем больше продажи, тем больше рейтинг" подтверждается')
else:
    print('Гипотеза "Чем больше продажи, тем больше рейтинг" не подтверждается')

if p_value_second < 0.05:
    print('Гипотеза "Рейтинг зависит от цены" подтверждается')
else:
    print('Гипотеза "Рейтинг зависит от цены" не подтверждается')

if p_value_first < 0.05 and p_value_second < 0.05:
    print('Гипотеза "Рейтинг зависит и от цены, и от количества проданных экземпляров" подтверждается')
else:
    print('Гипотеза "Рейтинг зависит и от цены, и от количества проданных экземпляров" не подтверждается')
```

Вывод в консоль:

```
Коэффициенты модели:
Intercept: 3.5141303303568496
How_Many_Sold: 6.643739639314892e-06
Current_Price: 0.00036761084744969287
Остаточная дисперсия: 0.14354685160891223
Доверительные интервалы для коэффициентов модели:
Intercept: 3.5031046164486304 - 3.525156044265069
How_Many_Sold: 6.192980454562006e-06 - 7.094498824067778e-06
Current_Price: 0.00035581125252048096 - 0.0003794104423789048
Коэффициент детерминации: 0.14898229821800515
Гипотеза "Чем больше продажи, тем больше рейтинг" подтверждается
Гипотеза "Рейтинг зависит от цены" подтверждается
Гипотеза "Рейтинг зависит и от цены, и от количества проданных экземпляров" подтверждается
```
