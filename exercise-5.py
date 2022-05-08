import math
from tabulate import tabulate


def f(x):
    return math.pow(x, 3) - 9 * math.pow(x, 2) - 6 * x + 96


def fd(x):
    return 3 * math.pow(x, 2) - 18 * x - 6


def fdd(x):
    return 6 * x - 18


def solve(l, r):
    table = []

    lr = f(l) * fdd(l)
    rr = f(r) * fdd(r)

    if lr >= 0:
        x = l
    elif rr >= 0:
        x = r
    else:
        raise Exception(f'At least one of {lr=} or {rr=} should be gte than 0.')

    i = -1
    while True:
        i += 1
        n_x = x - f(x) / fd(x)
        delta = round(abs(n_x - x), 3)
        table.append([
            i,
            round(x, 3),
            round(delta, 3),
        ])

        if delta <= 0.001:
            break

        x = n_x

    return table


if __name__ == '__main__':
    r1 = solve(-4, -3)
    print('[-4, -3]', '\n', tabulate(r1, headers=['i', 'x', 'delta']), '\n')

    r2 = solve(3, 4)
    print('[3, 4]', '\n', tabulate(r2, headers=['i', 'x', 'delta']), '\n')

    r3 = solve(8, 9)
    print('[8, 9]', '\n', tabulate(r3, headers=['i', 'x', 'delta']), '\n')
