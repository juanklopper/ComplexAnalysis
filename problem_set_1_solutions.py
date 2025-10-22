"""
Problem Set 1 Solutions
Complex Analysis Problems using NumPy and SciPy
"""

import numpy as np
from scipy import linalg

def print_problem(num, description, result):
    """Helper function to print problem results"""
    print(f"\n{'='*60}")
    print(f"Problem {num}")
    print(f"{description}")
    print(f"Result: {result}")
    print(f"{'='*60}")

def complex_to_polar(z):
    """Convert complex number to polar form (r, theta)"""
    r = np.abs(z)
    theta = np.angle(z)
    return r, theta

def polar_to_complex(r, theta):
    """Convert polar form to complex number"""
    return r * np.exp(1j * theta)

# Problem 1: (3 + 2i) + (-7 - i)
z1 = (3 + 2j) + (-7 - 1j)
print_problem(1, "(3 + 2i) + (-7 - i)", z1)

# Problem 2: [(5 + 3i) + (-1 + 2i)] - (7 - 5i)
z2 = ((5 + 3j) + (-1 + 2j)) - (7 - 5j)
print_problem(2, "[(5 + 3i) + (-1 + 2i)] - (7 - 5i)", z2)

# Problem 3: (5 + 3i) + [(-1 + 2i) - (7 - 5i)]
z3 = (5 + 3j) + ((-1 + 2j) - (7 - 5j))
print_problem(3, "(5 + 3i) + [(-1 + 2i) - (7 - 5i)]", z3)

# Problem 4: (2 - 3i)(4 + 2i)
z4 = (2 - 3j) * (4 + 2j)
print_problem(4, "(2 - 3i)(4 + 2i)", z4)

# Problem 5: (4 + 2i)(2 - 3i)
z5 = (4 + 2j) * (2 - 3j)
print_problem(5, "(4 + 2i)(2 - 3i)", z5)

# Problem 6: (2 - i)[(-3 + 2i)(5 - 4i)]
z6 = (2 - 1j) * ((-3 + 2j) * (5 - 4j))
print_problem(6, "(2 - i)[(-3 + 2i)(5 - 4i)]", z6)

# Problem 7: [(2 - i)(-3 + 2i)](5 - 4i)
z7 = ((2 - 1j) * (-3 + 2j)) * (5 - 4j)
print_problem(7, "[(2 - i)(-3 + 2i)](5 - 4i)", z7)

# Problem 8: (-1 + 2i)[(7 - 5i) + (-3 + 4i)]
z8 = (-1 + 2j) * ((7 - 5j) + (-3 + 4j))
print_problem(8, "(-1 + 2i)[(7 - 5i) + (-3 + 4i)]", z8)

# Problem 9: Let z1 = 2 + i, z2 = 3 - 2i. Calculate |3z1 - 4z2|
z1_p9 = 2 + 1j
z2_p9 = 3 - 2j
result_p9 = 3 * z1_p9 - 4 * z2_p9
magnitude_p9 = np.abs(result_p9)
print_problem(9, "Let z1 = 2 + i, z2 = 3 - 2i. Calculate |3z1 - 4z2|",
              f"{result_p9}, |3z1 - 4z2| = {magnitude_p9}")

# Problem 10: Let z = 2 + i. Calculate z³ - 3z² + 4z - 8
z_p10 = 2 + 1j
result_p10 = z_p10**3 - 3*z_p10**2 + 4*z_p10 - 8
print_problem(10, "Let z = 2 + i. Calculate z³ - 3z² + 4z - 8", result_p10)

# Problem 11: Let z = -1/2 + (√3/2)i. Calculate z⁴
z_p11 = -1/2 + (np.sqrt(3)/2)*1j
result_p11 = z_p11**4
print_problem(11, "Let z = -1/2 + (√3/2)i. Calculate z⁴", result_p11)

# Problem 12: Find x and y if 3x + 2yi - ix + 5y = 7 + 5i
# Rearranging: (3x + 5y) + i(-x + 2y) = 7 + 5i
# This gives us two equations:
# 3x + 5y = 7
# -x + 2y = 5
A = np.array([[3, 5], [-1, 2]])
b = np.array([7, 5])
solution_p12 = linalg.solve(A, b)
x_p12, y_p12 = solution_p12
print_problem(12, "Find x and y if 3x + 2yi - ix + 5y = 7 + 5i",
              f"x = {x_p12}, y = {y_p12}")

# Problem 13: Express 2 + 2√3 i in polar form
z_p13 = 2 + 2*np.sqrt(3)*1j
r_p13, theta_p13 = complex_to_polar(z_p13)
print_problem(13, "Express 2 + 2√3 i in polar form",
              f"r = {r_p13}, θ = {theta_p13} rad = {theta_p13/np.pi}π rad\n" +
              f"Polar form: {r_p13}e^(i·{theta_p13/np.pi}π)")

# Problem 14: Express -5 + 5i in polar form
z_p14 = -5 + 5j
r_p14, theta_p14 = complex_to_polar(z_p14)
print_problem(14, "Express -5 + 5i in polar form",
              f"r = {r_p14:.6f}, θ = {theta_p14} rad = {theta_p14/np.pi}π rad\n" +
              f"Polar form: {r_p14:.6f}e^(i·{theta_p14/np.pi}π)")

# Problem 15: Express 3e^(πi/2) in rectangular form
r_p15 = 3
theta_p15 = np.pi / 2
z_p15 = polar_to_complex(r_p15, theta_p15)
print_problem(15, "Express 3e^(πi/2) in rectangular form",
              f"{z_p15}\n" +
              f"Real part: {z_p15.real:.10f} ≈ 0\n" +
              f"Imaginary part: {z_p15.imag:.10f} = 3")

# Summary
print("\n" + "="*60)
print("SUMMARY OF ALL SOLUTIONS")
print("="*60)
solutions = {
    "Problem 1": z1,
    "Problem 2": z2,
    "Problem 3": z3,
    "Problem 4": z4,
    "Problem 5": z5,
    "Problem 6": z6,
    "Problem 7": z7,
    "Problem 8": z8,
    "Problem 9": f"|3z1 - 4z2| = {magnitude_p9}",
    "Problem 10": result_p10,
    "Problem 11": result_p11,
    "Problem 12": f"x = {x_p12}, y = {y_p12}",
    "Problem 13": f"{r_p13}e^(i·π/3)",
    "Problem 14": f"{r_p14:.6f}e^(i·3π/4)",
    "Problem 15": "0 + 3i"
}

for problem, solution in solutions.items():
    print(f"{problem}: {solution}")
print("="*60)
