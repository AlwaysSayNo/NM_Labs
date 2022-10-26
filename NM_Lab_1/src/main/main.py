import common.common as common
import dichotomy_method.dichotomy as dichotomy
import newton_method.newton as newton

epsilon = 10**-4
a = 2
b = 3.5
x_0 = a
x_star = b

print()
print(f"Check sign change condition on segment [{a}, {b}] = {common.sign_change_condition(a, b)}\n\n")

print("==> Dichotomy method")


apriori_n = dichotomy.apriori_assessment(a, b, epsilon)
print(f'Apriori assessment: {apriori_n}')

x, iteration = dichotomy.method(a, b, epsilon)

print(f'X_{iteration} with epsilon {epsilon} = {x}\n')



print("==> Newton method")

m_1 = newton.get_m_1(a)
m_2 = newton.get_m_2(b)
q = newton.get_q(x_0, x_star, newton.get_m_1(a), newton.get_m_2(b))

print(f'm_1 = {m_1}, m_2 = {m_2}, q = {q}')

apriori_n = newton.apriori_assessment(a, b, q, epsilon)
print(f'Apriori assessment: {apriori_n}')

x, iteration = newton.method(a, b, x_0, x_star, epsilon)
print(f'X_{iteration} with epsilon {epsilon} = {x}\n')