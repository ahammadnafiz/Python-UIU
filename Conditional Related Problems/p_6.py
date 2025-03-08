n = int(input())

if n > 0:
    if (n & (n - 1)) == 0:
        print("Yes")
    else:
        print("No")
else:
    if n == 0:
        print("Zero is not a valid input")
    else:
        print("Negetive input is not valid")
