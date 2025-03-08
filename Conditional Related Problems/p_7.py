a, b = map(int, input().split())

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is less than {b}")
