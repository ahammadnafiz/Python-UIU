def str_length(string: str) -> int:
    l = 0
    for i in string:
        l += 1
    return l


def find_substr(a: str, b: str) -> bool:
    len_a = str_length(a)
    len_b = str_length(b)
    for i in range(len_a - len_b + 1):
        if a[i : len_b + 1] == b:
            return True
    return False


def main():
    a, b = [i for i in input().split()]
    if find_substr(a, b):
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()