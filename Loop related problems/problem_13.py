n = int(input())

f = 1
for i in range(1, n + 1):
    f *= i

fibo = []
for j in range(n, 0, -1):
    fibo.append(j)

ans = []
for v in range(len(fibo)):
    ans.append(fibo[v])
    if v < len(fibo) - 1:
        ans.append('X')
    
print(f'{n}! = {' '.join(map(str, ans))} = {f}')