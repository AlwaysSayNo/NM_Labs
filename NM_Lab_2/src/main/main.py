import src.main.common.common as common
import src.main.tridiagonal_method.tridiagonal as tridiagonal
import src.main.jacobi_method.jacobi as jacobi


n = 4
matrix = [
    [4, 2, 0, 0],
    [1, 5, 2, 0],
    [0, 3, 7, 3],
    [0, 0, 2, 9]
]
values = [0, 3, 5, 1]
epsilon = 0.001


print("==> Tridiagonal method\n")

# matrix = tridiagonal.build_tridiagonal_matrix(4, 10)
# values = common.build_vector(4, 10)

print(f"Matrix ({n}x{n}):")
common.print_matrix(matrix)
print(f"Values: \n{values}\n")

print("Check tridiagonal consistency:")
check_consistency = tridiagonal.check_tridiagonal_consistency(matrix)
print(f"Tridiagonal consistency is {check_consistency}\n")

if check_consistency:
    result, _ = tridiagonal.find_result(matrix, values)
    print(f"Result vector: {result}")

    print(f"{result[0] * matrix[0][0] + result[1] * matrix[0][1] + result[2] * matrix[0][2] + result[3] * matrix[0][3]} = {values[0]}")
    print(f"{result[0] * matrix[1][0] + result[1] * matrix[1][1] + result[2] * matrix[1][2] + result[3] * matrix[1][3]} = {values[1]}")
    print(f"{result[0] * matrix[2][0] + result[1] * matrix[2][1] + result[2] * matrix[2][2] + result[3] * matrix[2][3]} = {values[2]}")
    print(f"{result[0] * matrix[3][0] + result[1] * matrix[3][1] + result[2] * matrix[3][2] + result[3] * matrix[3][3]} = {values[3]}")

    det = tridiagonal.find_determinant(matrix, values)
    print(f"\nDeterminant: {det}")
else:
    print("The sequence is inconsistent")


print("\n\n########################################################")
print("########################################################\n\n")


print("==> Jacobi method\n")

print(f"Matrix ({n}x{n}):")
common.print_matrix(matrix)
print(f"Values: \n{values}\n")

print("Check Jacobi consistency:")
check_consistency = jacobi.check_jacobi_consistency(matrix)
print(f"Tridiagonal consistency is {check_consistency}\n")

result = jacobi.find_result(matrix, values, epsilon)
print(f"\nResult vector: {result}")


print("\n\n########################################################")
print("########################################################\n\n")


print(f"Conditionality number")
print(common.conditionality_number(matrix))

print(f"{result[0] * matrix[0][0] + result[1] * matrix[0][1] + result[2] * matrix[0][2] + result[3] * matrix[0][3]} = {values[0]}")
print(f"{result[0] * matrix[1][0] + result[1] * matrix[1][1] + result[2] * matrix[1][2] + result[3] * matrix[1][3]} = {values[1]}")
print(f"{result[0] * matrix[2][0] + result[1] * matrix[2][1] + result[2] * matrix[2][2] + result[3] * matrix[2][3]} = {values[2]}")
print(f"{result[0] * matrix[3][0] + result[1] * matrix[3][1] + result[2] * matrix[3][2] + result[3] * matrix[3][3]} = {values[3]}")