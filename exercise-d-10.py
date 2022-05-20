import math


def f(x, y):
    return math.cos(y) / (1.25 + x) - 0.1 * y ** 2


h = 0.1

x, y = 0, 0
i = -1
while True:
    i += 1

    k1 = f(x, y)
    k2 = f(x + h / 2, y + h / 2 * k1)
    k3 = f(x + h / 2, y + h / 2 * k2)
    k4 = f(x + h, y + h * k3)

    yn = round(y + h / 6 * (k1 + k2 + k3 + k4), 2)
    delta = round(abs(y - yn), 2)
    print(f'{i=} {x=:.2f} {y=:.2f} {yn=} {delta=}')
    if delta <= 0.01:
        break
    x += h
    y = yn

print('')

# Адамс
pppx, pppy = 0, 0
ppx, ppy = 0, 0
px, py = 0.1, 0.05
x, y = 0.2, 0.1

i = -1
while True:
    i += 1
    yn = y + h / 24 * (55 * f(x, y) - 59 * f(px, py) + 37 * f(ppx, ppy) - 9 * f(pppx, pppy))
    delta = round(abs(y - yn), 2)
    print(f'{i=} {y=:.2f} {x=:.2f} {delta=}')
    if delta <= 0.01:
        break
    y, py, ppy, pppy = yn, y, py, ppy
    x += h

"""
i=0 x=0.00 y=0.00 yn=0.05 delta=0.05
i=1 x=0.10 y=0.05 yn=0.1 delta=0.05
i=2 x=0.20 y=0.10 yn=0.14 delta=0.04
i=3 x=0.30 y=0.14 yn=0.18 delta=0.04
i=4 x=0.40 y=0.18 yn=0.22 delta=0.04
i=5 x=0.50 y=0.22 yn=0.26 delta=0.04
i=6 x=0.60 y=0.26 yn=0.29 delta=0.03
i=7 x=0.70 y=0.29 yn=0.32 delta=0.03
i=8 x=0.80 y=0.32 yn=0.35 delta=0.03
i=9 x=0.90 y=0.35 yn=0.38 delta=0.03
i=10 x=1.00 y=0.38 yn=0.41 delta=0.03
i=11 x=1.10 y=0.41 yn=0.43 delta=0.02
i=12 x=1.20 y=0.43 yn=0.45 delta=0.02
i=13 x=1.30 y=0.45 yn=0.47 delta=0.02
i=14 x=1.40 y=0.47 yn=0.49 delta=0.02
i=15 x=1.50 y=0.49 yn=0.51 delta=0.02
i=16 x=1.60 y=0.51 yn=0.53 delta=0.02
i=17 x=1.70 y=0.53 yn=0.55 delta=0.02
i=18 x=1.80 y=0.55 yn=0.57 delta=0.02
i=19 x=1.90 y=0.57 yn=0.59 delta=0.02
i=20 x=2.00 y=0.59 yn=0.6 delta=0.01

i=0 y=0.10 x=0.20 delta=0.07
i=1 y=0.17 x=0.30 delta=0.06
i=2 y=0.23 x=0.40 delta=0.05
i=3 y=0.27 x=0.50 delta=0.04
i=4 y=0.31 x=0.60 delta=0.03
i=5 y=0.35 x=0.70 delta=0.03
i=6 y=0.37 x=0.80 delta=0.02
i=7 y=0.39 x=0.90 delta=0.01
"""