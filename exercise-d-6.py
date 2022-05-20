def solve(m):

    h = [0] * len(m)
    for i in range(1, len(m)):
        h[i] = m[i][0] - m[i-1][0]

    Y = [0] * len(m)
    for i in range(1, len(m) - 1):
        l = (m[i + 1][1] - m[i][1]) / h[i + 1]
        r = (m[i][1] - m[i - 1][1]) / h[i]
        Y[i] = l - r

    P, Q = [0] * len(m), [0] * len(m)
    for i in range(2, len(m) - 1):
        P[i] = h[i + 1] / (2 * (h[i] + h[i + 1]) + P[i] * h[i])
        Q[i] = (6 * Y[i] - h[i] * Q[i]) / (2 * (h[i] + h[i+1]) + P[i] * h[i])

    M = [0] * len(m)
    for i in range(len(m) - 1, 0, -1):
        M[i-1] = P[i] * Q[i]

    for i in range(len(M)):
        print(f'm[{i}] = {M[i]}')


if __name__ == '__main__':
    matrix = [[1.410, 0.888551],
              [1.416, 0.889559],
              [1.422, 0.890637],
              [1.428, 0.891667],
              [1.434, 0.892687],
              [1.440, 0.893698]]

    solve(matrix)

"""
m[0] = 0
m[1] = -0.4705882352945879
m[2] = -0.0980392156858277
m[3] = -0.08823529411800789
m[4] = 0
m[5] = 0
"""