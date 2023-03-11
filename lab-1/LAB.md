### Лабораторная работа №1.
---
#### <p style="text-align: center"> Задача №1. </p>
Найдем минимальный объем выборки $n$ равномерно для $\theta \in E$, где выборочное среднее отличается от математического ожидания $\mu_{0}$ не более чем на $\varepsilon > 0$, где $\varepsilon = 0.01$, с вероятностью не меньшей $1 - \sigma$, $\sigma \in (0, 1)$, где $\sigma = 0.05$.

$$n = \frac{Z^2  p  q} {\varepsilon^2}$$

$n - $объем выборки
$Z - $коэффициент, зависящий от выбранного исследователем доверительного уровня
$p - $доля респондентов с наличием исследуемого признака
$q = 1 - p - $доля респондентов, у которых исследуемый признак отсутствует
$\varepsilon - $предельная ошибка выборки

___Доверительный уровень___ - это вероятность того, что реальная доля лежит в границах полученного доверительного интервала: выборная доля $(p) \pm$ ошибка выборки $(\varepsilon)$. Доверительный уровень устанавливает сам исследователь в соответствии со своими требованиями к надежности полученных результатов. Чаще всего применяются доверительные уровни, равные $0.95$ или $0.99$. В маркетинговых исследованиях, как правило, выбирается доверительный уровень, равный $0.95$. При этом уровне $Z$ равен $1.96$.

__Код__

импортируемые библиотеки
``` python
import math
import random
import numpy as np
import matplotlib.pyplot as plt
```

класс интервала
``` python
class Interval:
    def __init__(self, right, left):
        self.left = left
        self.right = right
```

константы
``` python
Z = 1.96
p = 0.95
q = 0.05
e = 0.01
param = 2/3
```

функция Бернулли
``` python
def Bern(p) -> bool:
    return random.uniform(0.0, 1.0) <= p
```

основная функция
``` python
if __name__ == '__main__':
    Z = round(list(scipy.stats.norm.interval(0.95))[1], 2)
    print(Z)
    # находим объем выборки по формуле
    n = math.ceil(((Z**2)*p*q)/(e**2))
    # выводим объем выборки
    print(n)

    # создаем пустой массив
    sample = np.zeros((500, n), dtype=bool)
    print(sample)

    # запоняем массив данными
    for i in range(500):
        for j in range(n):
            sample[i][j] = False + Bern(param)

    print()

    # выводим массив
    print(sample)

    m_0 = param

    interval = Interval(m_0+e, m_0-e)

    answers = np.zeros((1, 500), dtype=float)

    # находим количество значений отличающихся от математического ожидания
    k = 0
    for i in range(500):
        sum = 0
        for j in range(n):
            sum = sum + sample[i][j]
        temp = sum / n
        answers[0][i] = temp
        if temp < interval.left or temp > interval.right:
            k = k + 1

    print(k)

    fig = plt.figure(figsize=(0, 1))
    ax = fig.add_subplot()

    ax.hist(answers[0])
    ax.grid()

    plt.show()
```

__Вывод в косоль__
```
1825
[[False False False ... False False False]
 [False False False ... False False False]
 [False False False ... False False False]
 ...
 [False False False ... False False False]
 [False False False ... False False False]
 [False False False ... False False False]]

[[False  True  True ... False  True  True]
 [False  True  True ... False  True  True]
 [False False  True ...  True False False]
 ...
 [ True  True False ...  True False False]
 [ True  True  True ...  True  True  True]
 [ True  True False ... False  True  True]]
168
```

__Гистограмма__
![1](https://github.com/georgedem975/mathematical_statistics/blob/master/lab-1/assets/Figure_1.png)

---

#### <p style="text-align: center"> Задача №2. </p>

__Код__

подключаемся к csv
``` python
data = pd.read_csv("")
```

находим начальные данные о телефонах
``` python
print(sum(data['dual_sim']))
print(sum(data['three_g']))
print(max(data['n_cores']))
```

считываем данные о емкости аккумулятора
``` python
container = data['battery_power']
container_with_wf = data['battery_power'][data.wifi != 0]
container_without_wf = data['battery_power'][data.wifi == 0]
```

находим выборочное среднее
``` python
container_sample_average = round(sum(container)/len(container), 1)
container_with_wf_sample_average = round(sum(container_with_wf)/len(container_with_wf), 1)
container_without_wf_sample_average = round(sum(container_without_wf)/len(container_without_wf), 1)

print(container_sample_average)
print(container_with_wf_sample_average)
print(container_without_wf_sample_average)
```

находим выборочную дисперсию
``` python
print(np.var(container))
print(np.var(container_with_wf))
print(np.var(container_without_wf))
```

находим выборочную медиану
``` python
print(np.median(container))
print(np.median(container_with_wf))
print(np.median(container_without_wf))
```

находим выборочную квантиль
``` python
print(container.quantile(np.arange(0.01, 0.4, 0.01)))
print(container_with_wf.quantile(np.arange(0.01, 0.4, 0.01)))
print(container_without_wf.quantile(np.arange(0.01, 0.4, 0.01)))
```

строим график эмпирической функции
``` python
fig, axs = plt.subplots(3)

ecdf_1 = ECDF(container)
axs[0].step(ecdf_1.x, ecdf_1.y)
plt.ylabel('$F(x)$', fontsize=20)
plt.xlabel('$x$', fontsize=20)

ecdf_2 = ECDF(container_with_wf)
axs[1].step(ecdf_2.x, ecdf_2.y)
plt.ylabel('$F(x)$', fontsize=20)
plt.xlabel('$x$', fontsize=20)

ecdf_3 = ECDF(container_without_wf)
axs[2].step(ecdf_3.x, ecdf_3.y)
plt.ylabel('$F(x)$', fontsize=20)
plt.xlabel('$x$', fontsize=20)

plt.show()
```

строим гистограмму
``` python
fig, axs = plt.subplots(3)

axs[0].hist(container)
axs[0].grid()

axs[1].hist(container_with_wf)
axs[1].grid()

axs[2].hist(container_without_wf)
axs[2].grid()

plt.show()
```

строим box-plot
``` python
fig, axs = plt.subplots(3)

axs[0].boxplot(container)

axs[1].boxplot(container_with_wf)

axs[2].boxplot(container_without_wf)

plt.show()
```

__Вывод в консоль__
```
1019
1523
8
1238.5
1234.9
1242.2
192991.81565775
190108.7314801847
195929.52475838206
1226.0
1233.0
1222.0
0.01     510.00
0.02     524.96
0.03     538.97
0.04     556.92
0.05     570.95
0.06     583.94
0.07     596.00
0.08     609.00
0.09     618.00
0.10     634.90
0.11     648.00
0.12     664.88
0.13     675.87
0.14     693.58
0.15     709.85
0.16     720.00
0.17     730.00
0.18     752.82
0.19     769.00
0.20     781.00
0.21     798.00
0.22     813.56
0.23     826.00
0.24     837.76
0.25     851.75
0.26     864.00
0.27     878.73
0.28     895.72
0.29     911.00
0.30     920.70
0.31     938.76
0.32     957.68
0.33     972.00
0.34     987.00
0.35    1002.00
0.36    1020.00
0.37    1037.26
0.38    1053.62
0.39    1065.00
Name: battery_power, dtype: float64
0.01     511.13
0.02     519.26
0.03     549.17
0.04     560.52
0.05     576.65
0.06     585.56
0.07     594.91
0.08     610.08
0.09     622.17
0.10     641.60
0.11     660.86
0.12     673.00
0.13     685.00
0.14     704.00
0.15     711.85
0.16     720.08
0.17     730.00
0.18     750.38
0.19     768.47
0.20     775.60
0.21     793.73
0.22     808.00
0.23     825.99
0.24     833.00
0.25     844.25
0.26     857.52
0.27     867.02
0.28     881.64
0.29     895.77
0.30     912.00
0.31     932.06
0.32     948.00
0.33     966.00
0.34     984.68
0.35    1001.55
0.36    1020.00
0.37    1034.81
0.38    1047.88
0.39    1062.07
Name: battery_power, dtype: float64
0.01     508.85
0.02     526.40
0.03     535.00
0.04     546.40
0.05     565.00
0.06     583.10
0.07     597.90
0.08     605.00
0.09     618.00
0.10     629.00
0.11     642.00
0.12     654.60
0.13     671.00
0.14     685.70
0.15     708.25
0.16     721.20
0.17     731.90
0.18     753.30
0.19     771.00
0.20     790.00
0.21     802.00
0.22     816.70
0.23     826.00
0.24     841.40
0.25     858.50
0.26     874.10
0.27     896.85
0.28     909.00
0.29     915.00
0.30     929.00
0.31     952.05
0.32     964.20
0.33     980.05
0.34     988.80
0.35    1006.00
0.36    1019.80
0.37    1040.35
0.38    1061.30
0.39    1067.15
Name: battery_power, dtype: float64
```

__Графики__

<p style="text-align:center">эмпирическая функция распредаления</p>

![2](https://github.com/georgedem975/mathematical_statistics/blob/master/lab-1/assets/Figure_2.png)

<p style="text-align:center">гистограмма</p>

![3](https://github.com/georgedem975/mathematical_statistics/blob/master/lab-1/assets/Figure_3.png)

<p style="text-align:center">box-plot</p>

![4](https://github.com/georgedem975/mathematical_statistics/blob/master/lab-1/assets/Figure_4.png)

---

___Ключевые понятия___

* Закон больших чисел (слабый, для независимых одинаково распределенных случайных величин)

Пусть $X_1, ..., X_n$ являются $i.i.d.$ случайными величинами с $E X_i = \mu$ и $Var X_i = \sigma^2 < \infty$. Пусть $\overline{X_n}$ является соответствующим выборочным средним. Тогда для любого $\epsilon > 0$:

<tex>$$\lim_{n \rightarrow \infty} P(|\overline{X_n} - \mu | < \epsilon) = 1$$<tex>

В таком случае мы говорим, что $\overline{X_n}$ сходится к $\mu$ по вероятности.

Доказательство:

Рассмотрим неравенство Чебышова

<tex>$$ P(g(\overline{X_n}) >= r ) <= {{E \cdot g(\overline{X_n})} \over{r}}, g(\overline{X_n}) = (\overline{X_n} - \mu)^2, r = \epsilon^2 \Longrightarrow $$<tex>

<tex>$$ \Longrightarrow P((\overline{X_n} - \mu)^2 >= \epsilon^2) <= {{Var{\overline{X_n}} \over {\epsilon^2}}} = {{\sigma}^2 \over {n \cdot \epsilon^2}} $$<tex>

<tex>$$ \Longrightarrow P(|\overline{X_n} - \mu | >= \epsilon) <= {{\sigma}^2 \over {n \cdot \epsilon^2}} $$<tex>

<tex>$$ P(|\overline{X_n} - \mu | >= \epsilon) = 1 - P(|\overline{X_n} - \mu| < \epsilon) $$<tex>

<tex>$$ \Longrightarrow \lim_{n \rightarrow \infty}P(|\overline{X_n} - \mu| < \epsilon) >= \lim_{n \rightarrow \infty} (1 - {{\sigma}^2 \over {n \cdot \epsilon^2}}) $$<tex>

<tex>$$  \Longrightarrow \lim_{n \rightarrow \infty}P(|\overline{X_n} - \mu| < \epsilon) = 1$$<tex>

* Центральная предельная теорема (для независимых одинаково распределенных случайных величин)

Пусть $X_1, ..., X_n$ являются $i.i.d.$ случайными величинами с $E X_i = \mu$ и $Var X_i = \sigma^2 < \infty$. Пусть $\overline{X_n}$ является соответствующим выборочным средним. Пусть $G_n(x)$ обозначает кумулятивную функцию распределения случайной величины.

<tex>$$ Z_n = \sqrt{n} \cdot {{\overline{X_n} - \mu } \over { \sigma } } $$<tex>

Тогда для любого $x \in R$ мы имеем:

<tex>$$ \lim_{n \rightarrow \infty} G_n(x) = \int_{- \infty}^x {{1} \over {\sqrt{2\pi}}} \cdot \exp({{y^2} \over {2}})dy, $$<tex>

То есть $Z_n$ сходится к $n(0, 1)$ по распределению:

<tex>$$ \sqrt{n} \cdot {{\overline{X_n} - \mu} \over {\sigma}} \rightarrow n(0, 1). $$<tex>

Распределение для $\overline {X_n}$:

<tex>$$ Z_n = \sqrt{n} \cdot {{\overline{X_n} - \mu} \over {\sigma}} \Longrightarrow \overline{X_n} = \mu + {{\sigma} \over {\sqrt{n}}}Z_n \Longrightarrow \overline{X_n} \sim n(\mu, {{\sigma^2} \over {n}}) $$<tex>

* Предположения на выборку

Статистическая гипотеза — гипотеза о виде распределения и свойствах случайной величины, которое можно подтвердить или опровергнуть применением статистических методов к данным выборки.

* Эмпирическая функция распределения, её состоятельность

Функция распределения - функция, которая определяет вероятность события $X \leq x$, то есть $F(x) = P(X \leq x)$

Эмпирическая функция распределения - функция, которая определяет для каждого $x$ частоту события $X \leq x$, то есть $$ \hat{F_n}(x) = \hat{P}(X \leq x) = {{1} \over {n}} \sum_{i=1}^n [X_i \leq x]$$

где [ ] - индикаторная функция, то есть:

$$[X_i \leq x ] = {\begin{equation*} \Bigl\{ \begin{aligned}
    1, X_i \leq x \\
    0, иначе
\end{aligned} 
\end{equation*}}
 $$

1. Несмещенноость: $E(\hat{F_n}(x)) = F_X(x)$

2. Состоятельность: $\lim_{n \rightarrow \infty} \hat{F_n}(x) = F_X(x)$

3. Ассимптотическая нормальность: $\hat{F_n}(x) \sim N(F_X(x), {{F_X(x)\cdot(1-F_X(x))}\over{n}})$

* Выборочное среднее, его несмещенность, состоятельность и асимптотическая нормальность

Выборочное (эмпирическое) среднее - это приближение теоритического среднего распределения, основанное на выборке из него.

Определение: Пусть $X_1, ..., X_n$ - выборка из распределения вероятности, определенная на некотором вероятностном пространстве. Тогда ее выборочным средним называется случайная величина: $$\overline{X} = {{1}\over{n}}\sum_{i=1}^n X_i$$

Выборочное среднее - несмещенная оценка теоретического среднего: $$E[\overline{X}] = E[X_i], i = 1, ..., n$$

Выборочное среднее - сильно состоятельная оценка теоритического среднего: $$\overline{X} \rightarrow E[X_i], n \rightarrow \infty$$

Выборочное среднее - ассимптотически нормальная оценка. Пусть дисперсия случайных величин $X_i$ конечна и ненулевая, то есть $D[X_i] = \sigma^2 < \infty, \sigma^2 \ne 0, i = 1, ..., n$

Тогда $\overline{X} - E[X_1] \rightarrow N(0, \sigma^2), n \rightarrow \infty$

где $N(0, \sigma^2)$ - нормальное распределение со средним $0$ и дисперсией $\sigma^2$

* Смещенная и несмещенная выборочная дисперсия

Пусть $X_1, ..., X_n, ...$ - выборка из распределения вероятности. Тогда:

1. Выборочная дисперсия - это случайная величина:

<tex>$$ S_n^2 = {{1}\over{n}} \sum_{i=1}^n (X_i - \overline{X})^2 =  {{1}\over{n}} \sum_{i=1}^n X_i^2 - ({{1} \over{n}} \sum_{i=1}^n X_i)^2, $$<tex>

где $\overline{X}$ обозначает выборочное среднее

2. несмещенная (исправленная) дисперсия - это случайная величина:

<tex>$$S^2 = {{1}\over{n - 1}} \sum_{i=1}^n (X_i - \overline{X})^2$$<tex>

* Теоретическая (в том числе непрерывный случай) и выборочная квантили

Кванти́ль в математической статистике — значение, которое заданная случайная величина не превышает с фиксированной вероятностью. Если вероятность задана в процентах, то квантиль называется процентилем или перцентилем.

Например, фраза «90-й процентиль массы тела у новорожденных мальчиков составляет 4 кг» означает, что 90 % мальчиков рождаются с весом, меньшим либо равным 4 кг, а 10 % мальчиков рождаются с весом, большим либо равным 4 кг.

Рассмотрим вероятностное пространство ${\displaystyle (\Omega ,\;{\mathcal {F}},\;\mathbb {P} )}$ и ${\displaystyle \mathbb {P} ^{X}}$ — вероятностная мера, задающая распределение некоторой случайной величины ${\displaystyle X}$. Пусть фиксировано ${\displaystyle \alpha \in (0,\;1)}$. Тогда ${\displaystyle \alpha }$ -квантилем или квантилем уровня ${\displaystyle \alpha }$ распределения ${\displaystyle \mathbb {P} ^{X}}$ называется число ${\displaystyle x_{\alpha }\in \mathbb {R} }$, такое что

<tex>$${\displaystyle \mathbb {P} (X\leqslant x_{\alpha })\leqslant \alpha }, \\
{\displaystyle \mathbb {P} (X\geqslant x_{\alpha })\geqslant 1-\alpha .}$$<tex>

В некоторых источниках (например, в англоязычной литературе) ${\displaystyle k}$-м ${\displaystyle q}$-квантилем называется квантиль уровня ${\displaystyle k/q}$, то есть ${\displaystyle (k/q)}$-квантиль в предыдущих обозначениях.

* Выборочная медиана

Выборочная медиана - результат наблюдения, занимающий центральное место в вариационном ряду, построенном по выборке с нечетным числом элементов, или полусумма двух результатов наблюдений, занимающих два центральных места в вариационном ряду, построенном по выборке с четным числом элементов.