n, r = list(map(int, input().split()))

f_n = 1
for i in range(1, n + 1):
    f_n *= i

f_r = 1
for j in range(1, r + 1):
    f_r *= j

f_n_r = n - r
f_nr = 1
for k in range(1, f_n_r + 1):
    f_nr *= k

nCr = f_n / (f_r * f_nr)
print(nCr)