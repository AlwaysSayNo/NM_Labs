from random import seed
from random import randint
import numpy as np

# tridiagonal (n=4, border=10, seed=36. 115, 120)
# jacobi (n=4, border=10, seed=7. 210, 352)
seed(7)


def build_matrix(n, border):
    arr = []

    for i in range(n):
        row = []
        for j in range(n):
            elem = get_rand_double(border)
            row.append(elem)

        arr.append(row)

    return arr


def build_vector(n, border):
    vector = []

    for i in range(n):
        vector.append(get_rand_double(border))

    return vector


def get_rand_double(border):
    return randint(0, border - 1) * 1.0


def print_matrix(matrix):
    for row in matrix:
        print("|", end='')

        curr_i = 0
        for elem in row:
            print('{:>5.2f}'.format(elem), end='')

            if curr_i != len(row) - 1:
                print(",", end='')
            curr_i += 1

        print(" |")


def find_seed_for_matrix(start, matrix_func, check_func, *args):
    i = start
    while True:
        print(f"{i}")
        seed(i)
        matrix = matrix_func(*args)
        print_matrix(matrix)

        check = check_func(matrix)
        if not check:
            i += 1
        else:
            return i


def vector_cubic_norm(vector):
    max_elem = -1

    for elem in vector:
        tmp = abs(elem)
        if max_elem < tmp:
            max_elem = tmp

    return max_elem


def matrix_cubic_norm(matrix):
    vector = []

    for row in matrix:
        sum_elems = 0

        for elem in row:
            sum_elems += abs(elem)

        vector.append(sum_elems)

    return vector_cubic_norm(vector)


def subtract_vectors(lhs, rhs):
    result = []
    for i in range(len(lhs)):
        result.append(lhs[i] - rhs[i])

    return result


def conditionality_number(matrix):
    matrix_inverted = np.linalg.inv(matrix)

    m_norm = matrix_cubic_norm(matrix)
    m_inverted_norm = matrix_cubic_norm(matrix_inverted)

    return m_norm * m_inverted_norm
