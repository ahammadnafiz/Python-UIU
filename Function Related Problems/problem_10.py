def sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    arr = [int(i) for i in input().split()]
    print(f'{' '.join(map(str, sort(arr)))}')
    
if __name__ == '__main__':
    main()