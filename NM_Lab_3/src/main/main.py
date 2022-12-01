from lagrange_method.lagrange import calculate_approximate_value
from lagrange_method.lagrange import calculate_approximate_value_inverse
from common.common import calculate_f

func = calculate_f
a = 3
b = 4
n = 10


res = calculate_approximate_value(calculate_f, a, b, n)
print(f"Direct lagrange method: {res}")

res = calculate_approximate_value_inverse(calculate_f, a, b, n)
print(f"Inverse lagrange method: {res}")
