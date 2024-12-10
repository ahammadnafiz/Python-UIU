n = int(input())
c = n + 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(c):
        print('_', end='')
    if i == n:
        for j in range(i - 1, 0, -1):
            print(j, end='')
    else:
        for j in range(i, 0, -1):
            print(j, end='')
    c -= 2
    print()