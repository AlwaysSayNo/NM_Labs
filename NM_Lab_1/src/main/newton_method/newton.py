import math
import src.main.common.common as common


def apriori_assessment(x_0, x_star, q, eps):
    """
    n_0(eps) = [log_2((ln(|x_0 - x_*|) / eps) / ln(1/q)) + 1] + 1
    """
    inner_log = math.log(abs(x_0 - x_star) / eps, math.e) / math.log(1 / q, math.e)
    return math.floor(inner_log + 1) + 1


def split_on_segments(a, b, n):
    arr = []
    step = (a + b) / n
    for i in range(n + 1):
        arr.append(a + step * i)

    return arr


def diff_not_zero(a, b, rounds, n):
    segments = split_on_segments(a, b, n)

    prev = common.diff_f(segments[0], rounds)

    for i in range(1, n + 1):
        curr = common.diff_f(segments[i], rounds)

        if not prev * curr > 0:
            return False

    return True


def get_m_1(x):
    return common.diff_f(x, 1)


def get_m_2(x):
    return common.diff_f(x, 2)


def get_q(x_0, x_star, m_1, m_2):
    return m_2 * abs(x_0 - x_star) / (2 * m_1)


def method(a, b, x_0, x_star, eps):
    """
    Calculating the newton method
    """
    if not common.sign_change_condition(a, b) \
            or not diff_not_zero(a, b, 1, 10) \
            or not diff_not_zero(a, b, 2, 10) \
            or not common.sign_change_condition_2(x_0):
        raise Exception("Invalid args")

    m_1 = get_m_1(a)
    m_2 = get_m_2(b)

    q = get_q(x_0, x_star, m_1, m_2)
    if not (0 < q < 1):
        raise Exception("Invalid args")

    iteration = 0
    x = x_0

    while True:
        x_prev = x
        x -= common.diff_f(x, 0) / common.diff_f(x, 1)

        print('{:<2d}: x_{:<2d} = {:<10f}, x_{:<2d} = {:<10f}'.format(iteration, iteration, x_prev, iteration + 1, x))

        iteration = iteration + 1
        if common.termination_condition(x, x_prev, eps):
            break

    return x, iteration
