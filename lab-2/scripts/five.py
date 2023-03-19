import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def bias(theta_0, x):
    func = lambda x, theta: 3 * x ** 2 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (theta - x ** 3) ** 2)
    int = lambda x: x ** 3 * func(x, theta_0)
    result = quad(int, -np.inf, np.inf)[0]
    return result - theta_0


def var(theta_0, x):
    b = bias(theta_0**2, x)
    return b - bias(theta_0, x)**2


def mse(theta_0, x):
    return var(theta_0, x) + bias(theta_0, x)**2


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