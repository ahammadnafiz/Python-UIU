def is_prime(n: int) -> bool:
    prime = True
    
    if n < 2:
        prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i  == 0:
                prime = False
                break
    return prime


def main():
    n = int(input())
    if is_prime(n):
        print('Prime')
    else:
        print('Not Prime')

if __name__ == '__main__':
    main()