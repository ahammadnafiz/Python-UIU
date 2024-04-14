def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def pascal(n):
    for i in range(n + 1):
        for j in range(n - i + 1):
            print(end=' ')
        for k in range(i + 1):
            ele = factorial(i)/(factorial(k) * factorial(i - k))
            print(int(ele), end=' ')
        print()

def main():
    n = int(input())
    pascal(n)

if __name__ == '__main__':
    main()