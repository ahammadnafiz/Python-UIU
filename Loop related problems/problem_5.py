x, y = map(int, input().split())

if x == y:
    print('Reached!')
elif x < y:
    for i in range(x, y + 1):
        print(i ** 2, end=',')
    else:
        print('Reached!', end=' ')
else:
    for i in range(x, y, -1):
        print(i ** 2, end=',')
    else:
        print('Reached!', end=' ')