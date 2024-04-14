x = float(input())
convergence_threshold = 1e-10

result = 0
term = x
k = 1

while abs(term) > convergence_threshold:
    result += term
    term = term * - (x ** 2) / ((2 * k) * (2 * k + 1))
    k += 1

print(f"{result:.10f}")
