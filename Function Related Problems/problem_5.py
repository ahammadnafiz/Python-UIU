def swap(a:int, b:int) -> None:
    a, b = b, a
    print(f'Value in func: {' '.join(map(str, (a, b)))}')
    
    
def main() -> None:
    a, b = map(int, input().split())
    swap(a, b)
    print(f'Value in Main: {' '.join(map(str, (a, b)))}')
    
    
if __name__ == '__main__':
    main()