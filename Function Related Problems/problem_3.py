def sum_func(n:list)->int:
    s = 0
    for i in range(len(n)):
        s += n[i]
    return f'Sum In Function: {s}'

def main()->None:
    n = [int(i) for i in input().split()]
    print(sum_func(n))
    s = 0
    for i in range(len(n)):
        s += n[i]
    print(f'Sum In Main: {s}')

if __name__ == '__main__':
    main()