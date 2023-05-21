import pandas as pd
import numpy as np

data = pd.read_csv('path')

X = data[['How_Many_Sold', 'Current_Price']]
y = data['RATING']

X['How_Many_Sold'] = X['How_Many_Sold'].str.replace(',', '').astype(float)
X['Current_Price'] = X['Current_Price'].str.replace('₹', '').str.replace(',', '').astype(float)
X = X.replace([np.inf, -np.inf], np.nan).fillna(0)

X['intercept'] = 1

coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

print('Коэффициенты модели:')
print('Intercept:', coefficients[2])
print('How_Many_Sold:', coefficients[0])
print('Current_Price:', coefficients[1])

residuals = y - X.dot(coefficients)

residual_variance = np.var(residuals, ddof=X.shape[1])

print('Остаточная дисперсия:', residual_variance)

X_transpose_X_inverse = np.linalg.inv(X.transpose().dot(X))
standard_errors = np.sqrt(np.diagonal(residual_variance * X_transpose_X_inverse))

confidence_interval = 1.96 * standard_errors
lower_bounds = coefficients - confidence_interval
upper_bounds = coefficients + confidence_interval

print('Доверительные интервалы для коэффициентов модели:')
print('Intercept:', lower_bounds[2], '-', upper_bounds[2])
print('How_Many_Sold:', lower_bounds[0], '-', upper_bounds[0])
print('Current_Price:', lower_bounds[1], '-', upper_bounds[1])

total_sum_of_squares = np.sum((y - np.mean(y)) ** 2)
explained_sum_of_squares = np.sum((X.dot(coefficients) - np.mean(y)) ** 2)
r_squared = explained_sum_of_squares / total_sum_of_squares

print('Коэффициент детерминации:', r_squared)

if coefficients[0] > 0:
    print('Гипотеза "Чем больше продажи, тем больше рейтинг" подтверждается')
else:
    print('Гипотеза "Чем больше продажи, тем больше рейтинг" не подтверждается')

if coefficients[1] > 0:
    print('Гипотеза "Рейтинг зависит от цены" подтверждается')
else:
    print('Гипотеза "Рейтинг зависит от цены" не подтверждается')

if coefficients[0] > 0 and coefficients[1] > 0:
    print('Гипотеза "Рейтинг зависит и от цены, и от количества проданных экземпляров" подтверждается')
else:
    print('Гипотеза "Рейтинг зависит и от цены, и от количества проданных экземпляров" не подтверждается')