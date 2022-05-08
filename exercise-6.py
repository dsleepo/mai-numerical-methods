import matplotlib.pyplot as plt
import numpy as np
import math


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
    p = [
        [0.38, -0.41],
        [1.35, -1.07],
        [2.28, -2.20],
        [2.90, -3.18],
        [3.45, -3.15],
        [3.74, -3.87],
        [5.28, -4.99],
        [6.20, -6.14],
        [7.58, -6.98],
        [7.95, -7.44],
        [9.41, -8.92],
        [9.71, -9.84],
    ]
    [linear_f, linear_q, linear_a, linear_b] = solve_linear(p)
    print(f'Linear', '\n', f'a={linear_a}\nb={linear_b}\nQ={linear_q}\n')

    [quadratic_f, quadratic_q, quadratic_a, quadratic_b, quadratic_c] = solve_quadratic(p)
    print(f'Quadratic', '\n', f'a={quadratic_a}\nb={quadratic_b}\nc={quadratic_c}\nQ={quadratic_q}\n')

    fig, ax = plt.subplots()
    linspace = np.linspace(-30, 30, 50)
    ax.plot(linspace, [quadratic_f(px) for px in linspace], label='quadratic', marker='o',
            linewidth=1, markersize=2)
    ax.plot(linspace, [linear_f(px) for px in linspace], label='linear', marker='o',
            linewidth=1, markersize=2)
    ax.legend()
    ax.grid(True)
    plt.show()
