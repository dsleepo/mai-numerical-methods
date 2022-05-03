import math


def user_function(x):
    return math.pow(x - 1, 2) * math.log(x + 11, 10) - 1


def solve(a, b, iterations):
    sign_a = 1 if user_function(a) > 0 else -1
    sign_b = 1 if user_function(b) > 0 else -1

    if sign_a == sign_b:
        raise Exception(f'signA={sign_a} must not equal signB={sign_b}')

    for i in range(iterations):
        c = (a + b) / 2
        result = user_function(c)
        print(f'{i + 1}) a={a} b={b} c={c} r={result}')

        if result > 0:
            if sign_a > 0:
                a = c
            else:
                b = c
        else:
            if sign_a > 0:
                b = c
            else:
                a = c


if __name__ == '__main__':
    solve(1, 2, 10)
