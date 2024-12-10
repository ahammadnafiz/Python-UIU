n = int(input())
x = 1
for i in range(n):
    if i < n - 1:
        print(x, end=',')
        x += 2
print(x, end=' ')