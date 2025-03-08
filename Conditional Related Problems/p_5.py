# Bitwise Trick to Check if a Number is a Power of 2
n = int(input())

print("Yes" if n > 0 and (n & (n - 1)) == 0 else "No")
