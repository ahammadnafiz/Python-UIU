n = int(input())

for i in range(1, n + 1):
    for j in range(i, i*2):
        print(j, end='')
    print()