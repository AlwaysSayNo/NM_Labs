import math

import src.main.common.common as common


def build_jacobi_matrix(n, border):
    arr = []

    for i in range(n):
        row = []
        for j in range(n):
            elem = common.get_rand_double(border)

            if j == i:
                elem += math.ceil(border * 0.5)

            row.append(elem)

        arr.append(row)

    return arr


def check_jacobi_consistency(matrix):
    size = len(matrix)
    is_correct = True

    for i in range(size):
        diag, other = get_check_args(matrix, i)

        if is_diagonal_advantage(diag, other):
            print(get_check_stat_string([diag], other, i, ">"))
        else:
            print(get_check_stat_string([diag], other, i, "<="))
            is_correct = False
            break

    return is_correct


def get_check_args(matrix, curr_i):
    n = len(matrix)

    diag = matrix[curr_i][curr_i]
    other = []

    for i in range(n):
        if i != curr_i:
            elem = matrix[curr_i][i]
            other.append(elem)

    return diag, other


def is_diagonal_advantage(diag, other):
    rhs = 0

    for elem in other:
        rhs += abs(elem)

    return abs(diag) > rhs


def get_check_stat_string(lhs_list, rhs_list, i, sign):
    result_s = "{:d}. ".format(i)

    result_s = concat_elements(result_s, lhs_list, "+")
    result_s += " {:s} ".format(sign)
    result_s = concat_elements(result_s, rhs_list, "+")

    return result_s


def concat_elements(result_s, elements, sign):
    size = len(elements)
    for i in range(size):
        result_s += "|{:.1f}|".format(elements[i])

        if i != size - 1:
            result_s += " {:s} ".format(sign)

    return result_s


def get_x(matrix, values, curr_i, x_list):
    diag, other = get_check_args(matrix, curr_i)
    other.insert(curr_i, diag)
    result = values[curr_i]

    for i in range(len(matrix)):
        if i != curr_i:
            result += -other[i] * x_list[i]

    result /= diag

    return result


def is_stop_condition(x_list, prev_list, epsilon, i):
    vector = common.subtract_vectors(x_list, prev_list)
    norm = common.vector_cubic_norm(vector)

    print(f"Stop condition: ||x_({i+1}) - x_({i})|| = {norm} <= {epsilon} ==> {norm <= epsilon}")

    return norm <= epsilon


def find_result(matrix, values, epsilon):
    i = 0
    size = len(matrix)
    x_list = []
    prev_list = [0] * size

    while True:
        for j in range(size):
            x = get_x(matrix, values, j, prev_list)
            x_list.append(x)

        if is_stop_condition(x_list, prev_list, epsilon, i):
            break

        i += 1
        prev_list = x_list
        x_list = []

    return x_list


# it = common.find_seed_for_matrix(211, build_jacobi_matrix, check_jacobi_consistency, 4, 10)
