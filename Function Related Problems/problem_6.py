def swap(arr:list) -> None:
    arr[0], arr[1] = arr[1], arr[0]
    return arr

def main():
    arr = [int(i) for i in input().split()]
    print(f'Value in Func: {' '.join(map(str, swap(arr)))}')
    print(f'Value in Main: {' '.join(map(str, (arr[0], arr[1])))}')
    
if __name__ == '__main__':
    main()