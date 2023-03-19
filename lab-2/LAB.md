# Лабораторная работа №2
---
__Основное задание__

Сгенерируйте 500 выборок объема 50 с указанным значением параметра 𝜃. Сколько раз оценка отклонится от истинного значения параметра более чем на 0.01? То же самое сделать для объемов выборки 100, 500, 1000, 2500. Визуализируйте результат. Как объяснить полученный результат?

---
### Задание №5

__Постановка задачи:__

Найти оценку максимального правдоподобия параметра $\theta$ для распределения с плотностью:

<tex>$$f_{\theta}(x) = {{3x^2}\over{\sqrt{2\pi}}}exp(-{{(\theta-x^3)}^2\over{2}})$$<tex>

найти её смещение, дисперсию и среднеквадратическую ошибку. Какими свойствами обладает данная оценка? Эксперимент при $\theta = 5$.

__Решение:__

Для начала выведем формулу нахождения оценки максимального правдоподобия для распределения с данной плотностью.

переход к суммированию

<tex>$$\prod_{i=1}^n = {{3x_1^2\cdot3x_2^2\cdot...\cdot3x_n^2}\over{\sqrt{2\pi}\cdot \sqrt{2\pi}\cdot...\cdot\sqrt{2\pi}}} \cdot \exp \Biggl(\Biggl(-{{(\theta - x_1^3)^2}\over{2}}\Biggr)\cdot\Biggl(-{{(\theta - x_2^3)^2}\over{2}}\Biggr)\cdot...\cdot\Biggl(-{{(\theta - x_n^3)^2}\over{2}}\Biggr)\Biggr)=$$<tex>

<tex>$$={{3^n\cdot\prod\nolimits_{i=1}^n x_i^2}\over{(2\pi)^{{n}\over{2}}}}\cdot\exp\Biggl(\Biggl(-{{1}\over{2}}\Biggr)^n\cdot\prod_{i=1}^n(\theta-x_i^3)^2\Biggr)=\ln\Biggl({{3^n\cdot\sum\nolimits_{i=1}^n x_i^2}\over{(2\pi)^{{n}\over{2}}}}\cdot\exp\Biggl(\Biggl(-{{1}\over{2}}\Biggr)^n\cdot\sum_{i=1}^n(\theta-x_i^3)^2\Biggr)\Biggr)=$$<tex>

<tex>$$=\ln3^n+\ln\sum_{i=1}^nx_i^2-{{n}\over{2}}\ln(2\pi)+\Bigl(-{{1}\over{2}}\Bigr)^n\cdot\sum_{i=1}^n(\theta - x_i^3)^2=$$<tex>

оценка максимального правдоподобия

<tex>$${{\mathrm{d}(\ln3^n+2\ln\sum\nolimits_{i=1}^nx_i-{{n}\over{2}}\ln(2\pi)+\Bigl(-{{1}\over{2}}\Bigr)^n\cdot\sum\nolimits_{i=1}^n(\theta - x_i^3)^2)}\over{\mathrm{d}\theta}}=$$<tex>

<tex>$$=\Bigl(-{{1}\over{2}}\Bigr)^n\cdot\Bigl(\sum_{i=1}^n(\theta - x_i^3)^2\Bigr)_\theta'=\Bigl(-{{1}\over{2}}\Bigr)^n\cdot\Bigl(\sum_{i=1}^n2(\theta - x_i^3)\Bigr)$$<tex>

приравниваем к нулю

<tex>$$\Bigl(-{{1}\over{2}}\Bigr)^n\cdot\Bigl(\sum_{i=1}^n2(\theta - x_i^3)\Bigr) = 0,$$<tex>

так как $\Bigl(-{{1}\over{2}}\Bigr)^n \neq 0 \Longrightarrow \sum\nolimits_{i=1}^n2(\theta - x_i^3) = 0 \Longrightarrow \theta = \overline{X}^3$ 

__найдем смещение__

найдем матиматическое ожидание

для нахождения математического ожидания оценки максимального правдоподобия для плотности $f_{\theta}(x)$ с оценкой максимального правдоподобия $\overline{x}^3$ и параметром $\theta_0$, нужно взять интеграл:


<tex>$$E[\overline{x}^3] = \int_{-\infty}^{\infty}x^3 f_{\theta_0}(x) dx = \int_{-\infty}^{\infty}x^3 {{3x^2}\over{\sqrt{2\pi}}}exp(-{{(\theta_0-x^3)}^2\over{2}}) dx$$<tex>

здесь мы использовали параметр $\theta_0 = 5$

после этого мы можем найти смещение

<tex>$$E[\overline{x}^3]−θ_0$$<tex>

код:
```python
def bias(theta_0, x):
    func = lambda x, theta: 3 * x ** 2 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (theta - x ** 3) ** 2)
    int = lambda x: x ** 3 * func(x, theta_0)
    result = quad(int, -np.inf, np.inf)[0]
    return result - theta_0
```

__найдем дисперсию__

формула для нахождения дисперсии

<tex>$$Var(\hat{\theta}) = E[\hat\theta^2]-(E[\hat\theta])^2,$$<tex>

где где $\hat{\theta} = \overline{x}^3$ - оценка максимального правдоподобия, $E[\hat{\theta}]$ - математическое ожидание оценки максимального правдоподобия, а $E[\hat{\theta}^2]$ - математическое ожидание квадрата оценки максимального правдоподобия.

ранее мы уже находили мат ожидание, поэтому нам надо найти только математическое ожидание квадрата оценки максимального правдоподобия.

формула нахождения математического ожидания квадрата оценки максимального правдоподобия.

<tex>$$E[\hat\theta^2] = \int_{-\infty}^{\infty}\hat\theta^2 f_{\theta_0}(x) dx$$<tex>

код:
```python
def var(theta_0, x):
    b = bias(theta_0**2, x)
    return b - bias(theta_0, x)**2
```

__найдем среднеквадратическую ошибку__

<tex>$$MSE(\hat\theta) = E[(\hat\theta - \theta_0)^2] = E[\hat\theta^2 - 2\hat\theta\theta_0 + \theta_0^2] = $$<tex>

<tex>$$=E[\hat\theta^2]-2\theta E[\hat\theta]+\theta^2=E[\hat\theta^2]-E[\hat\theta]^2+E[\hat\theta]^2-2\hat\theta\theta_0 + \theta^2=$$<tex>

<tex>$$Var(\hat\theta) + (E[\hat\theta]-\theta)^2 = Var(\hat\theta) + Bias(\hat\theta)^2$$<tex>

дисперсия и смещение у нас есть

код:
```python
def mse(theta_0, x):
    return var(theta_0, x) + bias(theta_0, x)**2
```

__Код для решения основного задания__
```python
theta = 5
count_samples = 500
sample_sizes = [50, 100, 500, 1000, 2500]


dev = []

for sample_size in sample_sizes:
    count = 0
    for i in range(count_samples):
        sample = np.random.normal(loc=theta, size=sample_size)
        mean_sample = np.mean(sample)
        if np.abs(mean_sample - theta) > 0.01:
            count += 1
    dev.append(count)


plt.plot(sample_sizes, dev, 'o-')
plt.xlabel('размер выборки')
plt.ylabel('количество отклонений')
plt.title('график отклонений для е=0.01)')
plt.show()
```

![1](https://github.com/georgedem975/mathematical_statistics/blob/master/lab-2/assets/Figure_1.png)

### Задание №6

__Постановка задачи:__

С помощью метода моментов найти оценку параметра $\theta$ распределения с плотностью:

<tex>$$f_{\theta}(x)={{1}\over{(k-1)!\theta^k}}x^{k-1}e^{-x/\theta}\mathbb{1}(x > 0),$$<tex>

если $k \in N - $известный параметр. Какимим свойствами обладает данная оценка? Эксперимент при $\theta = 2, k = 3$.

__Решение:__


для нахождения оценки параметра $\theta$ с помощью метода моментов, нужно приравнять теоретический момент порядка $r$ (существующий в распределении) и его выборочный аналог на основе выборки $X_1, X_2, ..., X_n$ порядка $r$.

<tex>$$E(X^r) = \int_{0}^{\infty} x^r f_{\theta}(x) dx$$<tex>

заметим, что данная плотность соответствует гамма распределению, следовательно

<tex>$$E(X) = k\theta, \ \ E(X^2) = (k+1)k\theta^2$$<tex>

для 1 и 2 моментов:

<tex>$$\overline{X} = E(X) = k\theta$$<tex>

<tex>$${{1}\over{n}} \sum_{i=1}^{n} X_i^2 = E(X^2) = (k+1)k\theta^2$$<tex>

следовательно:

<tex>$$\theta = {{\overline{X}}\over{k}}$$<tex>

свойства:
1. несмещенность
2. состоятельность
3. эффективность
4. асимптотическая нормальность

__Код для решения основного задания__

```python
import numpy as np
import matplotlib.pyplot as plt

theta_0 = 2
k = 3

values = [50, 100, 500, 1000, 2500]

e = 0.01

res = []

for n in values:
    dev_count = 0
    for i in range(500):
        X = np.random.gamma(k, theta_0, size=n)
        theta_overline = np.mean(X) / k
        if abs(theta_overline - theta_0) > e:
            dev_count += 1

    res.append(dev_count)


plt.plot(values, res, 'bo-')
plt.xlabel('Размер выборки')
plt.ylabel('Количество отклонений')
plt.title('Отклонения оценки от истинного значения')
plt.show()
```

![2](https://github.com/georgedem975/mathematical_statistics/blob/master/lab-2/assets/Figure_2.png)

---

__Примечание__
используемые библиотеки:
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
```

---

### Ключевые понятия:

+ __Постановка задачи точечного оценивания параметров__

+ __Состоятельность, несмещенность, асимптотическая нормальность__

+ __Эффективность оценки, информация Фишера, неравенство Рао-Крамера__

+ __Метод моментов__

+ __Метод максимального правдоподобия__