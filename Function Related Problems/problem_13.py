from problem_11 import is_prime

def GenNthPrime(n: int) -> int:
    
    if n <= 0:
        print("N must be a positive integer")

    count = 0  # Counter for prime numbers
    num = 2    # Current number to check for primality

    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

def main():
    n = int(input())
    print(f'{n}th Prime: {GenNthPrime(n)}')
    
if __name__ == '__main__':
    main()