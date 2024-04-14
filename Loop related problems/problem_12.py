n = int(input())

a, b = 0, 1

for i in range(n):
    if i < n - 1:
        print(b, end=',')
        a, b = b, a + b
    else:
        print(b, end=' ')
    