from problem_11 import is_prime


def GeneratePrime(n: int) -> list:
    primes = []
    
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    n = int(input())
    print(f'Prime less than {n}: {','.join(map(str, GeneratePrime(n)))}')

if __name__ == '__main__':
    main()