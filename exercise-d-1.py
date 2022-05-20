import numpy as np

matrix = np.matrix([[6.67, -1.44, -0.18, 1.83],
                    [0.48, -1.24, 0.37, -0.84],
                    [0.86, 0.43, 1.64, 0.64]])

matrix[1] = np.subtract(matrix[1], np.multiply(matrix[0], 0.07))
matrix[2] = np.subtract(matrix[2], np.multiply(matrix[0], 0.13))
matrix[2] = np.subtract(matrix[2], np.multiply(matrix[1], -0.54))

matrix = matrix.round(2)
print(matrix)

x3 = -0.12 / 1.87
x2 = (0.97 + 0.38 * x3) / 1.14
x1 = (1.44 * x2 + 0.18 * x3 + 1.83) / 6.67

print(f'{x1=:.2f} {x2=:.2f} {x3=:.2f}')
"""
x1=0.45 x2=0.83 x3=-0.06
"""

r = np.linalg.solve([row[0:3] for row in matrix], [row[-1:] for row in matrix])
print(r)
'''
[[ 0.45256775]
 [ 0.83345671]
 [-0.06417112]]
'''


def f(x1, x2, x3):
    return [
        0 * x1 + 1.44 / 6.67 * x2 + 0.18 / 6.67 * x3 + 1.83 / 6.67,
        0.48 / 1.24 * x1 + 0 * x2 + 0.37 / 1.24 * x3 + 0.84 / 1.24,
        0.86 / -1.64 * x1 + 0.43 / -1.64 * x2 + 0 * x3 + 0.64 / 1.64
    ]


x1, x2, x3 = 1.83, -0.84, 0.64
while True:
    [n_x1, n_x2, n_x3] = f(x1, x2, x3)
    delta = round(max(
        abs(n_x1 - x1),
        abs(n_x2 - x2),
        abs(n_x3 - x3),
    ), 2)

    if delta <= 0.01:
        break

    x1, x2, x3 = n_x1, n_x2, n_x3

print(f'{x1=:.2f} {x2=:.2f} {x3=:.2f}')
"""
x1=0.45 x2=0.84 x3=-0.06
"""
