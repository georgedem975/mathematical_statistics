import math
import random
import numpy as np
import matplotlib.pyplot as plt


class Interval:
    def __init__(self, right, left):
        self.left = left
        self.right = right


Z = 1.96
p = 0.95
q = 0.05
e = 0.01
param = 2/3


def Bern(p) -> bool:
    return random.uniform(0.0, 1.0) <= p


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