import math
import numpy as np


def solve_linear(points):
    n = len(points)
    sum_x = sum([x for [x, y] in points])
    sum_y = sum([y for [x, y] in points])
    sum_x2 = sum([math.pow(x, 2) for [x, y] in points])
    sum_x_y = sum([x * y for [x, y] in points])

    linear_left = np.array([
        [sum_x2, sum_x],
        [sum_x, n]
    ])
    linear_right = np.array([
        sum_x_y,
        sum_y,
    ])
    [a, b] = np.linalg.solve(linear_left, linear_right)

    f = lambda x: a * x + b
    q = sum([math.pow(y - f(x), 2) for [x, y] in points])

    return [f, q, a, b]


def solve_quadratic(points):
    n = len(points)
    sum_x = sum([x for [x, y] in points])
    sum_y = sum([y for [x, y] in points])
    sum_x2 = sum([math.pow(x, 2) for [x, y] in points])
    sum_x3 = sum([math.pow(x, 3) for [x, y] in points])
    sum_x4 = sum([math.pow(x, 4) for [x, y] in points])
    sum_x_y = sum([x * y for [x, y] in points])
    sum_x2_y = sum([math.pow(x, 2) * y for [x, y] in points])

    quadratic_left = np.array([
        [sum_x4, sum_x3, sum_x2],
        [sum_x3, sum_x2, sum_x],
        [sum_x2, sum_x, n],
    ])
    quadratic_right = np.array([
        sum_x2_y,
        sum_x_y,
        sum_y,
    ])
    [a, b, c] = np.linalg.solve(quadratic_left, quadratic_right)
    f = lambda x: a * math.pow(x, 2) + b * x + c
    q = sum([math.pow(y - f(x), 2) for [x, y] in points])

    return [f, q, a, b, c]


if __name__ == '__main__':
    p = [[0, 2.2],
         [0.12, 2.0],
         [0.19, 2.2],
         [0.35, 3.2],
         [0.4, 2.6],
         [0.45, 3.8],
         [0.62, 4.5],
         [0.71, 3.2],
         [0.84, 2.8],
         [0.91, 5.0],
         [1.0, 3.0]]

    [linear_f, linear_q, linear_a, linear_b] = solve_linear(p)
    print(f'Linear\na={linear_a}\nb={linear_b}\nQ={linear_q}\n')

    [quadratic_f, quadratic_q, quadratic_a, quadratic_b, quadratic_c] = solve_quadratic(p)
    print(f'Quadratic\na={quadratic_a}\nb={quadratic_b}\nc={quadratic_c}\nQ={quadratic_q}\n')

"""
Linear
a=1.754513046733842
b=2.244752006250711
Q=5.807087477414419

Quadratic
a=-3.0916418759455073
b=4.904021110145975
c=1.756573913337594
Q=4.989738350599211
"""