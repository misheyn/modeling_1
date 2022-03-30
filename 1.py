import numpy as np
import matplotlib.pyplot as plt


def y(x):
    return np.arctan(2 * x) ** 2


def y_der_analytic(x):
    return (4 * np.arctan(2 * x)) / (1 + 4 * x ** 2)


def y_der_discrete(x):
    return (y(x + 0.01) - y(x)) / 0.01


N = 50

x = np.arange(0, N * 0.01, 0.01)
plt.plot(x, y(x), label='original')
plt.plot(x, y_der_analytic(x), '--', label='analytic derivative')
plt.plot(x, y_der_discrete(x), '--', label='discrete derivative')
plt.legend()
plt.grid()
plt.show()

print(y_der_analytic(x))
