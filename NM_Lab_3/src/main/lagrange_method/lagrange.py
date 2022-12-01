import sympy
from sympy import S


def calculate_approximate_value(func, a, b, n):
    x_values = get_x_values(a, b, n)
    f_values = get_f_values(func, x_values)

    x_sym = sympy.symbols('x')

    f_sym = lagrange_method(x_values, f_values, x_sym, n)

    res_x_values = [*sympy.solveset(f_sym, x_sym, domain=S.Reals)]

    return find_max_in_range(a, b, res_x_values)


def calculate_approximate_value_inverse(func, a, b, n):
    x_values = get_x_values(a, b, n)
    f_values = get_f_values(func, x_values)

    y_sym = sympy.symbols('y')

    f_sym = lagrange_method_inverse(x_values, f_values, y_sym, n)

    res_x_values = f_sym.evalf(subs={y_sym: 0})

    return res_x_values


def get_x_values(a, b, n):
    x_values = []
    step = (b - a) / n
    x_n = a

    for i in range(0, n):
        x_values.append(x_n)
        x_n += step

    return x_values


def get_f_values(func, x_values):
    f_values = []

    for x_i in x_values:
        res = func(x_i)
        f_values.append(res)

    return f_values


def lagrange_method(x_values, f_values, x_sym, n):
    f_sym = 0

    for i in range(0, n):
        numerator = f_values[i]
        denominator = 1

        for j in range(0, n):
            if i == j:
                continue

            numerator *= (x_sym - x_values[j])
            denominator *= (x_values[i] - x_values[j])

        f_sym += numerator / denominator

    return f_sym


def lagrange_method_inverse(x_values, f_values, y_sym, n):
    return lagrange_method(f_values, x_values, y_sym, n)


def find_max_in_range(a, b, arr):
    max_res = arr[0]

    for elem in arr:
        if a <= elem <= b and elem > max_res:
            max_res = elem

    return max_res
