import math
from tabulate import tabulate


def f(x):
    return math.pow(x - 1, 2) * math.log(x + 11, 10) - 1


def solve(a, b, iterations):
    sign_a = 1 if f(a) > 0 else -1
    sign_b = 1 if f(b) > 0 else -1

    if sign_a == sign_b:
        raise Exception(f'signA={sign_a} must not equal signB={sign_b}')

    table = []

    for n in range(iterations):
        x_n = (a + b) / 2
        f_x_n = f(x_n)

        table.append([
            n,
            round(a, 3),
            round(b, 3),
            round(x_n, 3),
            round(f_x_n, 3)
        ])

        if f_x_n > 0:
            if sign_a > 0:
                a = x_n
            else:
                b = x_n
        else:
            if sign_a > 0:
                b = x_n
            else:
                a = x_n

    return table


if __name__ == '__main__':
    result = solve(1, 2, 10)
    print(tabulate(result, headers=['n', 'a', 'b', 'x_n', 'f(x_n)']))
