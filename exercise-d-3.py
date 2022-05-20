import math
from tabulate import tabulate

def f(x):
    return -1 * math.pow(x, 3) + 208 * math.pow(x, 2) - 13907 * x + 294124


def fd(x):
    return -3 * math.pow(x, 2) + 416 * x - 13907


def fdd(x):
    return -6 * x + 416


def solve(l, r, precision=2):
    table = []

    lr = f(l) * fdd(l)
    rr = f(r) * fdd(r)

    if lr >= 0:
        x = l
    elif rr >= 0:
        x = r
    else:
        print(f'{l=} {r=}')
        raise Exception(f'At least one of {lr=} or {rr=} should be gte than 0.')

    i = -1
    while True:
        i += 1
        n_x = x - f(x) / fd(x)
        delta = round(abs(n_x - x), precision)
        table.append([
            i,
            round(x, precision),
            round(delta, precision),
        ])

        if delta <= math.pow(10, -precision):
            break

        x = n_x

    return table


if __name__ == '__main__':
    r1 = solve(43, 44)
    print('[43, 44]', '\n', tabulate(r1, headers=['i', 'x', 'delta']), '\n')

    r2 = solve(77, 78)
    print('[77, 78]', '\n', tabulate(r2, headers=['i', 'x', 'delta']), '\n')

    r3 = solve(87, 88)
    print('[87, 88]', '\n', tabulate(r3, headers=['i', 'x', 'delta']), '\n')

"""
[43, 44] 
   i      x    delta
---  -----  -------
  0  43        0.77
  1  43.77     0.03
  2  43.8      0 

[77, 78] 
   i      x    delta
---  -----  -------
  0  77        0.05
  1  77.05     0 

[87, 88] 
   i      x    delta
---  -----  -------
  0  88        0.78
  1  87.22     0.07
  2  87.15     0 
"""
