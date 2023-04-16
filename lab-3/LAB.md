### Задача 1. 
---
##### Условие:
Предъявите доверительный интервал уровня $1 − \alpha$ для указанного параметра при данных предположениях (с обоснованиями). Сгенерируйте $2$ выборки объёма объёма $25$ и посчитайте доверительный интервал. Повторить $1000$ раз. Посчитайте, сколько раз 95-процентный доверительный интервал покрывает реальное значение параметра. То же самое сделайте для объема выборки $10000$. Как изменился результат? Как объяснить?
Везде даны две независимые выборки $X, Y$ из нормальных распределений $N(\mu_1, \sigma_1^2),N(\mu_2, \sigma_2^2)$ объема $𝑛, 𝑚$ соответственно. Сначала указывается оцениваемая функция, потом данные об остальных параметрах, затем параметры эксперимента и подсказки.
<tex>$$\tau = \sigma_1^2/\sigma_2^2;  \ \mu_1, \ \mu_2 \ неизвестны; \mu_1=0, \mu_2=0, \sigma_1^2=2, \sigma_2^2 = 1; \ воспольуйтесь функцией$$<tex>

<tex>$${{n(m-1)Var(X)} \over {m(n-1)Var(Y)}},$$<tex>
где $Var(.)$ – выборочная смещенная дисперсия. Смотрите в сторону распределения Фишера.

##### Решение:

<tex>$${{n(m-1)Var(X)} \over {m(n-1)Var(Y)}},$$<tex>
где $Var(.)$ – выборочная смещенная дисперсия. Смотрите в сторону распределения Фишера.

Построим доверительный интервал для $\tau$ на уровне значимости $1-\alpha$.

Для этого воспользуемся распределением Фишера с $n-1$ и $m-1$ степенями свободы:

<tex>$${{n(m-1)Var(X)} \over {m(n-1)Var(Y)}} \sim F_{n-1,m-1}$$<tex>

Для построения доверительного интервала находим квантили распределения Фишера $F_{n-1,m-1}$ уровня $1-\frac{\alpha}{2}$ и $\frac{\alpha}{2}$, обозначим их через $f_{1-\alpha/2}(n-1,m-1)$ и $f_{\alpha/2}(n-1,m-1)$. Тогда доверительный интервал для $\tau$ на уровне значимости $1-\alpha$ имеет вид:

<tex>$$\Biggl[{{n(m-1)Var(X)} \over {m(n-1)Var(Y)}}\cdot {{1}\over{f_{1-a/2}(n-1, m-1)}}, {{n(m-1)Var(X)} \over {m(n-1)Var(Y)}}\cdot {{1}\over{f_{1-a/2}(n-1, m-1)}}\Biggl]$$<tex>

Теперь сгенерируем 2 выборки объема $25$ и посчитаем доверительный интервал $1000$ раз, чтобы определить, сколько раз 95-процентный доверительный интервал покрывает реальное значение параметра. Затем повторим этот процесс для выборки объема $10000$ и сравним результаты.


код:
```python
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
```

вывод:
```python
Для выборки объема 25 доверительный интервал покрывает реальное значение параметра в 0.530 случаях
Для выборки объема 10000 доверительный интервал покрывает реальное значение параметра в 960.000 случаях
```

---
---

### Задача №2
---
##### Условие:
Постройте асимптотический доверительный интервал уровня $1 - \alpha$ для указанного параметра. Проведите эксперимент по схеме, аналогичной первой задаче.
Сначала указывается класс распределений (однопараметрический) и оцениваемый параметр, затем параметры эксперимента и подсказки. $U[-\theta, \ \theta]; \ \theta; \ \theta=5;$ воспользуйтесь предельной теоремой об асимптотическом поведении крайних членов вариационного ряда.

##### Решение:

Используем то, что функция распределения случайной величины равна $F(x) = (x + \theta)/(2 \theta)$ для $x \in [-\theta, \theta]$, чтобы найти функцию распределения $X_{max}$:

<tex>$$F_{max}(x) = P(X_{max} \le x)=$$<tex>

<tex>$$= P(X_1 \le x, \ X_2 \le x, \dots, X_n \le x) =$$<tex>

<tex>$$= P(X_1 \le x) \cdot (X_2 \le x) \cdot \dots \cdot (X_n \le x) =$$<tex>

<tex>$$F(x)^n = \Biggl({{x + \theta} \over {2 \theta}}\Biggr)^n$$<tex>

Найдем квантили для $X_{max}$:

<tex>$$F_{max}(q_1) = 1 - {{\alpha} \over {2}}$$<tex>

<tex>$$\Biggl({{q_1 + \theta} \over {2 \theta}}\Biggr)^n = 1 - {{\alpha} \over {2}}$$<tex>

<tex>$$q_1 = 2 \theta \Biggl(1 - {{\alpha} \over {2}} \Biggr)^{{1} \over {n}} - \theta = \theta \Biggl[2\biggl(1 - {{\alpha} \over {2}}\biggr)^{{1}\over{n}} - 1\Biggr]$$<tex>

<tex>$$F_{max}(q_2) = {{\alpha} \over {2}}$$<tex>

<tex>$$\Biggl({{q_2 + \theta} \over {2 \theta}}\Biggr)^n = {{\alpha} \over {2}}$$<tex>

<tex>$$q_2 = 2 \theta \Biggl({{\alpha} \over {2}}\Biggr)^{{1} \over {n}} - \theta = \theta \Biggl[2\biggl({{\alpha} \over {2}} \biggr)^{{1} \over {n}} - 1 \Biggr]$$<tex>

Таким образом, получаем доверительный интервал для $\theta$:

<tex>$${{X_{max}} \over {2 (1 - {{\alpha} \over {2}})^{{1} \over {n}} - 1}} \le \theta \le {{X_{max}} \over {2({{\alpha} \over {2}})^{{1} \over{n}} - 1}}$$<tex>

Это неравенство получено из определения квантили:

<tex>$$P(X_{max} \le \theta_{{\alpha} \over {2}}) = 1 - {{\alpha} \over {2}}$$<tex>

<tex>$$P(X_{max} \le \theta_{1 - {{\alpha} \over {2}}}) = {{\alpha} \over {2}}$$<tex>

Перепишем их с использованием функции распределения $X_{max}$:

<tex>$$F_{max}(\theta_{{\alpha} \over {2}}) = 1 - {{\alpha} \over {2}}$$<tex>

<tex>$$F_{max}(\theta_{1 - {{\alpha} \over {2}}}) = {{\alpha} \over {2}}$$<tex>

Подставим выражение для $F_{max}$ в полученные уравнения:

<tex>$${{(q_1 + \theta)^n} \over {(2\theta)^n}} = 1 - {{\alpha} \over {2}}$$<tex>

<tex>$${{(q_2 + \theta)^n} \over {(2\theta)^n}} = {{\alpha} \over {2}}$$<tex>

Решим каждое уравнение относительно $\theta$:

<tex>$$(q_1 + \theta)^n = (2 \theta)^n (1 - {{\alpha} \over {2}})$$<tex>

<tex>$$(q_2 + \theta)^n = (2\theta)^n({{\alpha} \over {2}})$$<tex>

Возводя обе части уравнений в степень ${{1}\over{n}}$, получим:

<tex>$$q_1 + \theta = 2\theta(1 - {{\alpha} \over {2}})^{{1} \over {n}}$$<tex>

<tex>$$q_2 + \theta = 2\theta({{\alpha} \over {2}})^{{1}\over{n}}$$<tex>

Выразим $\theta$ из первого уравнения:

<tex>$$\theta = {{q_1} \over {2(1 - {{\alpha} \over {2}})^{{1} \over {n}} - 1}}$$<tex>

Выразим $\theta$ из второго уравнения:

<tex>$$\theta = {{q_2} \over {2({{\alpha} \over {2}})^{{1} \over {n}} - 1}}$$<tex>

Подставляем выражения для $\theta$ в неравенство по определению квантили:

<tex>$$P(X_{max} \le q_2) = {{\alpha} \over {2}}$$<tex>

<tex>$$P(X_{max} \ge q_1) = 1 - {{\alpha} \over {2}}$$<tex>

Получаем доверительный интервал для параметра $\theta$:

<tex>$${{X_{max}} \over {2 (1 - {{\alpha} \over {2}})^{{1} \over {n}} - 1}} \le \theta \le {{X_{max}} \over {2({{\alpha} \over {2}})^{{1} \over{n}} - 1}}$$<tex>

Этот доверительный интервал имеет уровень доверия $1 - \alpha$.

код:
``` python
import numpy as np


def get_the_number_of_coatings(sample_size : int, theta : int=5, number_of_repetitions : int=1000, alpha : float=0.05) -> int:
    number_of_coatings = 0
    for i in range(number_of_repetitions):
        sample = np.random.uniform(size=sample_size, low=-theta, high=theta)
        first = theta >= np.max(sample) / (2 * (1 - alpha / 2) ** (1 / sample_size) - 1)
        second = theta <= np.max(sample) / (2 * (alpha / 2) ** (1 / sample_size) - 1)

        if first and second:
            number_of_coatings += 1

    return number_of_coatings


if __name__ == '__main__':
    sample_size, theta, number_of_repetitions, alpha = 25, 5, 1000, 0.05
    print(f"sample_size: {sample_size}, number_of_coating: {get_the_number_of_coatings(sample_size=sample_size)}")
    sample_size = 10000
    print(f"sample_size: {sample_size}, number_of_coating: {get_the_number_of_coatings(sample_size=sample_size)}")
```

вывод:
```python
sample_size: 25, number_of_coating: 947
sample_size: 10000, number_of_coating: 970
```


---

__Ключевые понятия:__

+ Доверительные интервалы. Доверительные интервалы для параметров нормального
распределения. Теорема Фишера
+ Доверительные интервалы. ”Универсальный” рецепт.
+ Асимптотические доверительные интервалы. ”Обычный” рецепт.
+ Теоремы об асимптотическом поведении среднего и крайних членов вариационного ряда.