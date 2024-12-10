def sum_func(arr:list)->int:
    s = 0
    for i in arr:
        s += i
    return f"Sum In Function: {s}"

def main()->None:
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    print(sum_func(arr))
    print('Sum In Main:', sum(arr))
    
if __name__ == '__main__':
    main()