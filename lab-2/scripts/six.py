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