n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        print(0, end=',')
    else:
        if i < n:
            print(1, end=',')
        else:
            print(1, end=' ')