import math


def user_function(x):
    return math.pow(x, 3) + 0.4 * math.pow(x, 2) + 0.6 * x - 1.6


def user_function_derivative(x):
    return 3 * math.pow(x, 2) + 0.8 * x + 0.6


def solve_newton(a, b, epsilon=0.001):
    i = 0
    prev_x = b
    while True:
        i += 1
        curr_x = prev_x - user_function(prev_x) / user_function_derivative(prev_x)
        delta = round(abs(curr_x - prev_x), 3)
        print(f'{i}) prev_x={prev_x} curr_x={curr_x} delta={delta}')

        if delta <= epsilon:
            break

        prev_x = curr_x


def solve_hord(a, b, epsilon=0.001):
    i = 0
    prev_x = a
    while True:
        i += 1
        curr_x = prev_x - user_function(prev_x) / (user_function(b) - user_function(prev_x)) * (b - prev_x)
        delta = round(abs(curr_x - prev_x), 3)
        print(f'{i}) prev_x={prev_x} curr_x={curr_x} delta={delta}')

        if delta <= epsilon:
            break

        prev_x = curr_x

# prev_x=0.9019066040342637
# solve1(0, 1, 10)
print('')
solve_newton(0, 1, 0.001)
print('')
solve_hord(0, 1, 0.001)
