'''
Write a program that takes in two numbers as input. Next, find the GCD (greatest
common divisor) and the LCM (lowest common multiple) of these two numbers
'''

# Prompt the user to input two space-separated integers and assign them to variables a and b
a, b = list(map(int, input().split()))

# Store the original values of a and b
original_a = a
original_b = b

'''
GCD formula for calculating gcd
GCD(A, B) = GCD(B, A % B)

'''
# Calculate the GCD
while b:
    # Swap the values of a and b, and calculate the remainder of a divided by b
    a, b = b, a % b

# The final value of a is the calculated GCD
gcd = a


'''
LCM formula for calculatig lcm
LCM(A, B) = (A * B) // GCD(A, B)
'''

# Calculate the LCM using the original values of a and b
lcm = (original_a * original_b) // gcd

# Print the calculated GCD and LCM
print(f"GCD: {gcd}\nLCM: {lcm}")
