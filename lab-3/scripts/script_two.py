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