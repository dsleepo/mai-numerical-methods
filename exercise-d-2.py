from tabulate import tabulate
import numpy as np


def solve_iteration(m):
    p_i = []
    q_i = []

    p_prev, q_prev = 0, 0
    for [a, b, c, d] in m:
        p = -c / (b + a * p_prev)
        p_i.append(p)

        q = (d - a * q_prev) / (b + a * p_prev)
        q_i.append(q)
        p_prev, q_prev = p, q

    x_i = [
        q_i[-1]
    ]
    x_prev = q_i[-1]
    for i in range(len(m) - 2, -1, -1):
        x = q_i[i] + p_i[i] * x_prev
        x_i.append(x)
        x_prev = x
    x_i.reverse()

    return x_i


def f(x1, x2, x3, x4):
    return [
        0 * x1 + 1 / 4 * x2 + 0 * x3 + 0 * x4 + 10.4 / 8,
        1 / 6 * x1 + 0 * x2 + 1 / 3 * x3 + 0 * x4 + 6.7 / 6,
        0 * x1 - 1 / 5 * x2 + 0 * x3 + 2 / 5 * x4 + 14.5 / 10,
        0 * x1 + 0 * x2 + 1 / 6 * x3 + 0 * x4 + 10.5 / 6,
    ]


def solve_seidel(a, b):
    table = []

    [x, y, z, k] = b
    i = -1
    while True:
        i += 1

        x_r = f(x, y, z, k)
        p_x, x = x, x_r[0]

        y_r = f(x, y, z, k)
        p_y, y = y, y_r[1]

        z_r = f(x, y, z, k)
        p_z, z = z, z_r[2]

        k_r = f(x, y, z, k)
        p_k, k = k, k_r[3]

        delta = max([
            abs(p_x - x),
            abs(p_y - y),
            abs(p_z - z),
            abs(p_k - k),
        ])

        table.append([
            i,
            round(x, 2),
            round(y, 2),
            round(z, 2),
            round(k, 2),
            round(delta, 2),
        ])

        if round(delta, 2) <= 0.01:
            break

    return table


if __name__ == '__main__':
    matrix = [[0, 8, -2, 10.4],
              [-1, 6, -2, 6.7],
              [2, 10, -4, 14.5],
              [-1, 6, 0, 10.5]]
    iteration_result = solve_iteration(matrix)
    print("Iteration: ", np.asmatrix(iteration_result))

    seidel_result = solve_seidel([], [
        10.4 / 8,
        6.7 / 6,
        14.5 / 10,
        10.5 / 6,
    ])
    print("\nSeidel:\n", tabulate(seidel_result, headers=['i', 'x', 'y', 'z', 'k', 'delta']))

"""
Iteration:  [[1.81011561 2.04046243 1.86632948 2.06105491]]

Seidel:
   i     x     y     z     k    delta
---  ----  ----  ----  ----  -------
  0  1.58  1.86  1.78  2.05     0.75
  1  1.77  2     1.87  2.06     0.19
  2  1.8   2.04  1.87  2.06     0.04
  3  1.81  2.04  1.87  2.06     0.01
"""
