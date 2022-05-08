import math
from tabulate import tabulate
import numpy as np


def f(x, y):
    return [
        math.cos(y) + 2,
        0.8 - math.cos(x - 1)
    ]


def solve_simple_iteration(x, y):
    table = []

    i = -1
    while True:
        i += 1

        [n_x, n_y] = f(x, y)
        delta = max(
            abs(x - n_x),
            abs(y - n_y),
        )

        table.append([
            i,
            round(x, 3),
            round(y, 3),
            round(delta, 3)
        ])

        if round(delta, 3) <= 0.001:
            break

        x, y = n_x, n_y

    return table


def solve_newton(x, y):
    table = []

    f1_dx = lambda x, y: -1 * math.sin(x - 1)
    f1_dy = lambda x, y: 1

    f2_dx = lambda x, y: 1
    f2_dy = lambda x, y: math.sin(y)

    i = -1
    while True:
        i += 1

        J = [[f1_dx(x, y), f1_dy(x, y)],
             [f2_dx(x, y), f2_dy(x, y)]]

        sub1 = np.transpose([[x, y]])
        sub2 = np.linalg.inv(J)
        sub3 = np.transpose([[math.cos(x - 1) + y - 0.8, x - math.cos(y) - 2]])

        result = np.subtract(
            sub1,
            np.matmul(sub2, sub3)
        )

        [[n_x, n_y]] = np.transpose(result)

        delta = round(max(
            abs(n_x - x),
            abs(n_y - y)
        ), 3)

        table.append([
            i,
            round(x, 3),
            round(y, 3),
            delta,
        ])

        if delta <= 0.001:
            break

        x, y = n_x, n_y

    return table


if __name__ == '__main__':
    si_r = solve_simple_iteration(2.5, 0.5)
    print('Simple iteration', '\n', tabulate(si_r, headers=['i', 'x', 'y', 'delta']), '\n')

    newton_r = solve_newton(2.5, 0.5)
    print('Newton', '\n', tabulate(newton_r, headers=['i', 'x', 'y', 'delta']), '\n')
