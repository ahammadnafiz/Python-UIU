def even_numbers(arr:list) -> list:
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    return even

def main():
    arr = [int(i) for i in input().split()]
    print(f'{' '.join(map(str, even_numbers(arr)))}')

if __name__ == '__main__':
    main()