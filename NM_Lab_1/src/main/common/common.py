import math
from sympy import *


def calculate_f(x):
    """
    Calculates function: sh(x) − 12 * th(x) − 0.311
    """
    return math.sinh(x) - 12 * math.tanh(x) - 0.311


def f_exp():
    x = symbols('x')
    expected = sinh(x) - 12 * tanh(x) - 0.311
    return expected


def sign_change_condition(a, b):
    """
    Checks the condition: f(a) * f(b) < 0
    """
    return calculate_f(a) * calculate_f(b) < 0


def diff_f(value, rounds):
    x = symbols('x')
    f = diff(f_exp(), x, rounds)

    result = f.evalf(subs={x: value})
    return result


def sign_change_condition_2(x_0):
    """
    Checks the condition: f(a) * f``(b) < 0
    """
    return calculate_f(x_0) * diff_f(x_0, 2) < 0


def termination_condition(x_0, x_1, eps):
    return abs(x_1 - x_0) < eps
