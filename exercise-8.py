import math


def solve():
    a = -1
    b = 2
    n = 5
    h = 3 / (2 * n)
    x_i = [a + i * h for i in range(0, 11)]

    f = lambda x: abs(x - math.sqrt(math.pow(x, 2) + math.pow(x, 4)))

    return (h / 3) * (
            f(x_i[0]) + 4 * sum([f(x) for x in x_i[1:-1:2]]) + 2 * sum([f(x) for x in x_i[2:-1:2]]) + f(x_i[-1])
    )


if __name__ == '__main__':
    r = solve()
    print(f'{r=}')
