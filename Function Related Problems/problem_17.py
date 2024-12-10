def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    original_a = a
    original_b = b
    g = gcd(a, b)
    result = (original_a * original_b) // g
    return result

def main():
    a, b = [int(i) for i in input().split()]
    
    print(f'GCD: {gcd(a, b)}')
    print(f'LCM: {lcm(a, b)}')

if __name__ == '__main__':
    main()
    