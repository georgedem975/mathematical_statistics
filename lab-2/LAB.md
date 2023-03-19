# Лабораторная работа №2
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

так как $\Bigl(-{{1}\over{2}}\Bigr)^n \neq 0 \Longrightarrow \sum_{i=1}^n2(\theta - x_i^3) = 0 \Longrightarrow \theta = \overline{X}^3$ 

__найдем смещение__

найдем матиматическое ожидание

для нахождения математического ожидания оценки максимального правдоподобия для плотности $f_{\theta}(x)$ с оценкой максимального правдоподобия $\overline{x}^3$ и параметром $\theta_0$, нужно взять интеграл:


<tex>$$E[\overline{x}^3] = \int_{-\infty}^{\infty}x^3 f_{\theta_0}(x) dx \ = \int_{-\infty}^{\infty}x^3 {{3x^2}\over{\sqrt{2\pi}}}exp(-{{(\theta_0-x^3)}^2\over{2}}) dx$$<tex>

здесь мы использовали параметр $\theta_0 = 5$

после этого мы можем найти смещение

<tex>$$E[\overline{x}^3]−θ_0$$<tex>

__найдем дисперсию__



__найдем среднеквадратическую ошибку__



### Задание №6

__Постановка задачи:__

С помощью метода моментов найти оценку параметра $\theta$ распределения с плотностью:

<tex>$$f_{\theta}(x)={{1}\over{(k-1)!\theta^k}}x^{k-1}e^{-x/\theta}\mathbb{1}(x > 0),$$<tex>

если $k \in N - $известный параметр. Какимим свойствами обладает данная оценка? Эксперимент при $\theta = 2, k = 3$.

__Решение:__

---

### Ключевые понятия:

+ __Постановка задачи точечного оценивания параметров__

+ __Состоятельность, несмещенность, асимптотическая нормальность__

+ __Эффективность оценки, информация Фишера, неравенство Рао-Крамера__

+ __Метод моментов__

+ __Метод максимального правдоподобия__

