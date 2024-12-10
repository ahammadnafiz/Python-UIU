n = int(input())
m = ((n + 1) // 2)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == m or j == 1 or j == n:
            print('H', end=' ')
        else:
            print(' ', end=' ')
    print()