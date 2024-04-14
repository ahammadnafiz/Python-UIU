def min_val(arr:list) -> int:
    min_num = 0
    
    for i in range(len(arr)):
        if arr[i] < arr[min_num]:
            min_num = i
            
    return arr[min_num]


def main():
    arr = [int(i) for i in input().split()]
    print(f'Minimum Value: {min_val(arr)}')


if __name__ == '__main__':
    main()