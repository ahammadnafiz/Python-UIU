n = int(input())
m = ((n + 1) // 2)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == m or j == m or i + j == m + 1 or i - j == m - 1 or j - i == m - 1 or i + j == n + m:
            print('*', end='')
        else:
            print(' ', end='')
    print()