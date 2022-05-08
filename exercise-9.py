import math
from tabulate import tabulate


def f(t, y):
    return y * math.cos(t + math.pow(y, 2))


def solve_euler():
    table = []
    a, b, n = 0, 3, 10
    h = (b - a) / n

    y = 3
    for i in range(0, 11):
        t_i = a + i * h
        n_y = y + h * f(t_i, y)
        table.append([i, y])
        y = n_y

    return table


def k1(t, y):
    return y * math.cos(t + y ** 2)


def k2(t, y, h):
    k1_i = k1(t, y)
    return k1(t + h / 2, y + (h / 2) * k1_i)


def solve_runge_kutta():
    table = []

    a, b, n = 0, 3, 10
    h = (b - a) / n

    y = 3
    for i in range(0, 11):
        t_i = a + i * h
        n_y = y + (1 / 6) * h * (k1(t_i, y) + 2 * k2(t_i, y, h))
        table.append([i, y])
        y = n_y

    return table


if __name__ == '__main__':
    r_euler = solve_euler()
    print('Euler\n', tabulate(r_euler, headers=['i', 'y']), '\n')

    r_runge_kutta = solve_runge_kutta()
    print('Runge-Kutta\n', tabulate(r_runge_kutta, headers=['i', 'y']), '\n')
