import math
import src.main.common.common as common


def apriori_assessment(a, b, eps):
    """
    n_0(eps) = [log_2((b - a) / eps)] + 1
    """
    if not common.sign_change_condition(a, b):
        return None
    return math.floor(math.log2((b - a) / eps)) + 1


def method(a, b, eps):
    """
    Calculating the dichotomy method
    """
    if not common.sign_change_condition(a, b):
        return None, None

    iteration = 0
    x = a
    while True:
        x = (b + a) / 2

        print('{:<2d}: [a: {:<10f}, b: {:<10f}]'.format(iteration, a, b))

        if common.sign_change_condition(a, x):
            b = x
        else:
            a = x

        iteration = iteration + 1
        if iteration != 0 and common.termination_condition(a, b, eps):
            break

    return x, iteration
