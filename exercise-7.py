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


if __name__ == '__main__':
    matrix_newton = [
        [1, 0.8],
        [1.2, 2.2],
        [1.4, 2.9],
        [1.6, 4.0],
        [1.8, 5.2],
        [2.0, 5.8],
    ]
    r1 = solve_newton(1.1, matrix_newton)
    r2 = solve_newton(2.1, matrix_newton)
    print(f'Newton:\n{r1=}\n{r2=}\n')

    matrix_lagrange = [
        [0, 11],
        [1, 12],
        [3, 13],
        [6, 14],
    ]
    l1 = solve_lagrange(1, matrix_lagrange)
    print(f'Lagrange:\n{l1=}\n')

