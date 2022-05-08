import math
from tabulate import tabulate


def f(x):
    return math.pow(x, 3) + 0.4 * math.pow(x, 2) + 0.6 * x - 1.6


def fd(x):
    return 3 * math.pow(x, 2) + 0.8 * x + 0.6


def solve_newton(a, b, epsilon=0.001):
    table = []

    i = 0
    x = b
    while True:
        i += 1
        n_x = x - f(x) / fd(x)
        delta = round(abs(n_x - x), 3)
        table.append([i - 1, round(x, 3), round(f(x), 3), round(fd(x), 3), round(-1 * (f(x) / fd(x)), 3)])

        if delta <= epsilon:
            break

        x = n_x

    return table


def solve_hord(a, b, epsilon=0.001):
    table = []

    i = 0
    x = a
    while True:
        i += 1
        n_x = x - f(x) / (f(b) - f(x)) * (b - x)
        delta = round(abs(n_x - x), 3)
        table.append([
            i - 1,
            round(x, 3),
            round(f(x) / (f(b) - f(x)), 3),
            round((b - x), 3)
        ])

        if delta <= epsilon:
            break

        x = n_x

    return table

newton_r = solve_newton(0, 1, 0.001)
print('Ньютон', '\n', tabulate(newton_r, headers=['i', 'x_n', 'f(x_n)', 'fd(x_n)', '-1 * (f(x) / fd(x))']), '\n')

hord_r = solve_hord(0, 1, 0.001)
print('Хорд', '\n', tabulate(hord_r, headers=['i', 'x_n', '(f(x_n) / (f(b) - f(x_n)))', '(b - x_n)']), '\n')
