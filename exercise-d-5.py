def newton_r(m):
    assert len(m) > 0

    if len(m) == 1:
        return m[0][1]

    if len(m) == 2:
        [m1, m2] = m
        [x1, y1] = m1
        [x2, y2] = m2
        return (y2 - y1) / (x2 - x1)

    return (newton_r(m[1:]) - newton_r(m[:-1])) / (m[0][0] - m[-1][0])


def solve_newton(x, m):
    result = 0
    for i in range(len(m)):
        sub = 1
        for j in range(i):
            sub *= x - m[j][0]

        result += newton_r(m[0:(i + 1)]) * sub

    return result


def solve_lagrange(x, m):
    result = 0
    for i in range(len(m)):
        sub = m[i][1]

        for j in range(len(m)):
            if j == i:
                continue
            sub *= (x - m[j][0]) / (m[i][0] - m[j][0])

        result += sub

    return result


def delta_newton(x, m):
    y = solve_newton(x, m)

    mn = matrix.copy()
    mn.append([x, y])

    yn = solve_newton(x, mn)

    return abs(y - yn)


def delta_lagrange(x, m):
    y = solve_lagrange(x, m)

    mn = matrix.copy()
    mn.append([x, y])

    yn = solve_lagrange(x, mn)

    return abs(y - yn)


if __name__ == '__main__':
    matrix = [[1.410, 0.888551],
              [1.416, 0.889559],
              [1.422, 0.890637],
              [1.428, 0.891667],
              [1.434, 0.892687],
              [1.440, 0.893698]]

    delta_n = delta_newton(1.4258, matrix)
    print(f'Newton: delta={delta_n}')

    delta_l = delta_lagrange(1.4258, matrix)
    print(f'Lagrange: delta={delta_l}')

"""
Newton: delta=0.0002880932012345738
Lagrange: delta=0.0
"""
