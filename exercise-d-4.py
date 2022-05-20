import math


def f(x):
    return 5 * x - 8 * math.log(x, math.e) - 8


def fd(x):
    return 5 - (8 / x)


def fdd(x):
    return 8 / x ** 2


def g(x):
    return (8 + 8 * math.log(x, math.e)) / 5


def gd(x):
    return 8 / (5 * x)


def check_delta(x, xp, xpp, precision):
    if xp is None or xpp is None:
        return False

    val = ((x - xp) ** 2) / abs(2 * xp - x - xpp)
    return round(val, precision) < 10 ** -precision


def solve_simple(a, b, precision):
    if gd(a) < 1:
        x = a
    elif gd(b) < 1:
        x = b
    else:
        assert False

    xp, xpp = None, None
    while True:
        cond1 = gd(x) < 1
        cond2 = round(f(x), precision) < 10 ** -precision
        cond3 = check_delta(x, xp, xpp, precision)
        if cond1 and cond2 and cond3:
            break

        print(f'{x=} {xp=} {xpp=}')
        xn = round(g(x), precision)
        xp, xpp, x = x, xp, xn


def solve_half(a, b, iterations):
    assert f(a) < 0
    assert f(b) > 0

    for i in range(iterations):
        x = (a + b) / 2

        fx = f(x)
        print(f'{x=}')

        if fx == 0:
            break
        elif fx > 0:
            b = x
        else:
            a = x


def solve_newton(a, b, precision):
    if f(a) * fdd(a) >= 0:
        x = a
    elif f(b) * fdd(b) >= 0:
        x = b
    else:
        assert False

    while True:
        print(f'{x=}')
        xn = round(x - f(x) / fd(x), precision)
        if abs(xn - x) < 10 ** -precision:
            break
        x = xn


if __name__ == '__main__':
    print('simple')
    solve_simple(3, 4, 2)

    print('\nhalf')
    solve_half(3, 4, 6)

    print('\nnewton')
    solve_newton(3, 4, 2)

"""
simple
x=3 xp=None xpp=None
x=3.36 xp=3 xpp=None
x=3.54 xp=3.36 xpp=3
x=3.62 xp=3.54 xpp=3.36
x=3.66 xp=3.62 xpp=3.54
x=3.68 xp=3.66 xpp=3.62

half
x=3.5
x=3.75
x=3.625
x=3.6875
x=3.71875
x=3.703125

newton
x=4
x=3.7
x=3.69
"""