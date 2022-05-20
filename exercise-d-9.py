import math


def f(x):
    return math.log(x**2 + 2, math.e) / (x + 1)


if __name__ == '__main__':
    a, b, n = 0, 1, 5
    h = (b - a) / (2 * n)

    x_i = [a + i * h for i in range(0, 11)]

    p1 = f(x_i[0])
    p2 = 4 * sum([f(x) for x in x_i[1:-1:2]])
    p3 = 2 * sum([f(x) for x in x_i[2:-1:2]])
    p4 = f(x_i[-1])

    r = (h/3) * (p1 + p2 + p3 + p4)
    print(f'{r=:.4f}')

"""
r=0.5658
"""