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

