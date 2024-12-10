a, b = list(map(int, input().split()))

orinigal_a = a
orinigal_b = b

while b:
    a, b = b, a % b

gcd = a

lcm = (orinigal_a * orinigal_b) // gcd

print(f"GCD; {gcd}\nLCM: {lcm}")