# numpy.transponse()
from tabulate import tabulate


def norm1(matrix):
    rows = []

    for row in matrix:
        acc = 0
        for col in row:
            acc += abs(col)

        rows.append(acc)

    return max(rows)


def norm2(matrix):
    cols = []

    for i in range(len(matrix)):
        acc = 0
        for j in range(len(matrix[i])):
            acc += abs(matrix[j][i])

        cols.append(acc)

    return max(cols)


def f(x, y, z, k):
    return [
        0 * x + 0.3 * y + 0.14 * z + 0.2 * k - 1,
        0.11 * x + 0 * y - 0.41 * z - 0.1 * k - 1,
        0.1 * x + 0.1 * y + 0 * z + 0.13 * k + 2,
        0.13 * x - 0.4 * y - 0.2 * z + 0 * k + 0.1,
    ]


def solve_simple_iteration(a, b):
    table = []

    min_norm = min(
        norm1(a),
        norm1([b])
    )
    assert min_norm < 1

    [x, y, z, k] = b
    i = -1
    while True:
        i += 1

        [n_x, n_y, n_z, n_k] = f(x, y, z, k)
        delta = max(
            abs(x - n_x),
            abs(y - n_y),
            abs(z - n_z),
            abs(k - n_k),
        )

        table.append([
            i,
            round(x, 3),
            round(y, 3),
            round(z, 3),
            round(k, 3),
            round(delta, 3),
        ])

        if round(delta, 3) <= 0.001:
            break

        x, y, z, k = n_x, n_y, n_z, n_k

    return table

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
            round(x, 3),
            round(y, 3),
            round(z, 3),
            round(k, 3),
            round(delta, 3),
        ])

        if round(delta, 3) <= 0.001:
            break

    return table



# wolfram {{x-0.3y - 0.14z - 0.2k = - 1}, {-0.11x + y + 0.41z + 0.1k = -1}, {-0.1x-0.1y+z-0.13k=2}, {-0.13x+0.4y+0.2z+k=0.1}}
if __name__ == '__main__':
    a = [
        [0, 0.3, 0.14, 0.2],
        [0.11, 0, -0.41, -0.1],
        [0.1, 0.1, 0, 0.13],
        [0.13, -0.4, -0.2, 0],
    ]
    b = [-1, -1, 2, 0.1]

    si_r = solve_simple_iteration(a, b)
    print("Simple iteration", '\n', tabulate(si_r, headers=['i', 'x', 'y', 'z', 'k', 'delta']), '\n')

    seidel_r = solve_seidel(a, b)
    print('Seidel', '\n', tabulate(seidel_r, headers=['i', 'x', 'y', 'z', 'k', 'delta']), '\n')
