import src.main.common.common as common


def build_tridiagonal_matrix(n, border):
    arr = []

    for i in range(n):
        row = []

        for j in range(n):
            elem = 0

            if i == j:
                elem = common.get_rand_double(border) + 1
            elif j + 1 == i or j - 1 == i:
                elem = common.get_rand_double(border)

            row.append(elem)

        arr.append(row)

    return arr


def check_tridiagonal_consistency(matrix):
    size = len(matrix)
    is_correct = True
    is_more_condition = False

    for i in range(size):
        a, b, c = get_a_b_c(matrix, i)

        if is_second_condition(a, b, c):
            is_more_condition = True
            print(f"{i}. |{c}| > |{a}| + |{b}|")
        elif is_first_condition(a, b, c):
            print(f"{i}. |{c}| >= |{a}| + |{b}|")
        else:
            print(f"{i}. |{c}| < |{a}| + |{b}|")
            is_correct = False
            break

    return is_correct and is_more_condition


def get_a_b_c(matrix, i):
    size = len(matrix)
    a = b = c = 0

    c = -matrix[i][i]

    if i != 0:
        a = matrix[i][i - 1]

    if i != size - 1:
        b = matrix[i][i + 1]

    return a, b, c


def is_first_condition(a, b, c):
    return abs(c) >= (abs(a) + abs(b))


def is_second_condition(a, b, c):
    return abs(c) > (abs(a) + abs(b))


def convert_values(values):
    f_list = []
    for value in values:
        f_list.append(-value)

    return f_list


def find_coefficients(matrix, f_list):
    a_list = []
    b_list = []
    z_list = []

    size = len(matrix)

    for i in range(1, size):
        a_prev, b_prev, c_prev = get_a_b_c(matrix, i - 1)
        a, b, c = get_a_b_c(matrix, i)

        if i == 1:
            a_list.append(b_prev / c_prev)
            b_list.append(f_list[i] / c_prev)
        else:
            z_prev = z_list[i - 2]
            beta_prev = b_list[i - 2]
            f_prev = f_list[i - 2]

            a_list.append(b_prev / z_prev)
            b_list.append((f_prev + a_prev * beta_prev))

        z_list.append(c - a_list[i - 1] * a)

    return a_list, b_list, z_list


def find_result(matrix, values):
    f_list = convert_values(values)
    a_list, b_list, z_list = find_coefficients(matrix, f_list)

    y_list = []
    size = len(matrix)
    i = size - 2

    while i >= -1:
        y = 0

        if i == size - 2:
            y = (f_list[i] + a_list[i] * b_list[i]) / z_list[i]
        else:
            y = a_list[i + 1] * y_list[0] + b_list[i + 1]

        y_list.insert(0, y)
        i -= 1

    return y_list, z_list


def find_determinant(matrix, values):
    f_list = convert_values(values)
    x_list, z_list = find_result(matrix, f_list)
    _, _2, c = get_a_b_c(matrix, 0)

    det = -c

    for z in z_list:
        det *= -z

    return det

# i = common.find_seed_for_matrix(116, build_tridiagonal_matrix, check_tridiagonal_consistency, 4, 10)
