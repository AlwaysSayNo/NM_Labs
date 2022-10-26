import src.main.common.common as common
import src.main.tridiagonal_method.tridiagonal as tridiagonal
import src.main.jacobi_method.jacobi as jacobi


# print("==> Tridiagonal method\n")
#
n = 4
#
# matrix = tridiagonal.build_tridiagonal_matrix(4, 10)
# values = common.build_vector(4, 10)
#
# print(f"Matrix ({n}x{n}):")
# common.print_matrix(matrix)
# print(f"Values: {values}")
# print()
#
# print("Check tridiagonal consistency:")
# check_consistency = tridiagonal.check_tridiagonal_consistency(matrix)
# print(f"Tridiagonal consistency is {check_consistency}\n")
#
# if check_consistency:
#     result, _ = tridiagonal.find_result(matrix, values)
#     print(f"Result vector: {result}")
#
#     det = tridiagonal.find_determinant(matrix, values)
#     print(f"Determinant: {det}")
# else:
#     print("The sequence is inconsistent")


print("==> Jacobi method\n")

matrix = jacobi.build_jacobi_matrix(4, 10)
values = common.build_vector(4, 10)
epsilon = 0.01

print(f"Matrix ({n}x{n}):")
common.print_matrix(matrix)
print(f"Values: {values}")
print()

print("Check Jacobi consistency:")
check_consistency = jacobi.check_jacobi_consistency(matrix)
print(f"Tridiagonal consistency is {check_consistency}\n")

result = jacobi.find_result(matrix, values, epsilon)
print(result)