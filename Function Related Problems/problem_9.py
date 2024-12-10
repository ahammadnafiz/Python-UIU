def multiply(arr:list) -> list:
    return [ i * 2 for i in arr]

def main():
    arr = [int(i) for i in input().split()]
    print(f"{' '.join(map(str, multiply(arr)))}")
    
if __name__ == '__main__':
    main()