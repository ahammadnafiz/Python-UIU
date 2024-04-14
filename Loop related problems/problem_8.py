n = int(input())  
reversed_number = 0  

original_digits_count = len(str(n))  # Count the number of digits in the original number

while n > 0:  
    last_digit = n % 10  
    reversed_number = (reversed_number * 10) + last_digit  
    n //= 10  

# Format the reversed number to always have the same number of digits as the original input
formatted_reversed_number = f"{reversed_number:0{original_digits_count}}"

print(formatted_reversed_number)
