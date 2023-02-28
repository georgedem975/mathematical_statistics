import numpy as np
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt

#подключились к csv
data = pd.read_csv("")

#нашли начальные данные о телефонах
print(sum(data['dual_sim']))
print(sum(data['three_g']))
print(max(data['n_cores']))

#считали данные о емкости аккумуляторов
container = data['battery_power']
container_with_wf = data['battery_power'][data.wifi != 0]
container_without_wf = data['battery_power'][data.wifi == 0]

#находим выборочное среднее
container_sample_average = round(sum(container)/len(container), 1)
container_with_wf_sample_average = round(sum(container_with_wf)/len(container_with_wf), 1)
container_without_wf_sample_average = round(sum(container_without_wf)/len(container_without_wf), 1)

print(container_sample_average)
print(container_with_wf_sample_average)
print(container_without_wf_sample_average)

#находим выборочную дисперсию
print(np.var(container))
print(np.var(container_with_wf))
print(np.var(container_without_wf))

#находим выборочную медиану
print(np.median(container))
print(np.median(container_with_wf))
print(np.median(container_without_wf))


#находим выборочную квантиль
print(container.quantile(np.arange(0.01, 0.4, 0.01)))
print(container_with_wf.quantile(np.arange(0.01, 0.4, 0.01)))
print(container_without_wf.quantile(np.arange(0.01, 0.4, 0.01)))

#строим график эмпирической функции
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

#строим гистограмму
fig, axs = plt.subplots(3)

axs[0].hist(container)
axs[0].grid()

axs[1].hist(container_with_wf)
axs[1].grid()

axs[2].hist(container_without_wf)
axs[2].grid()

plt.show()

#строим box-plot
fig, axs = plt.subplots(3)

axs[0].boxplot(container)

axs[1].boxplot(container_with_wf)

axs[2].boxplot(container_without_wf)

#boxplot = data.boxplot(column=['battery_power'])
plt.show()