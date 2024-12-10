n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or i + j == 1 + n:
            print('*', end='')
        else:
            print(' ', end='')
    print()