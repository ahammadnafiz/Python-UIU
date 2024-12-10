n = int(input())

ans = []
dot = []

k = 2
for _ in range(n):
    dot.append(k)
    k += 1

for i in range(1, n + 1):
    a = (i ** 2) * dot[i -1]
    ans.append(a)

print(f'Result: {sum(ans)}')