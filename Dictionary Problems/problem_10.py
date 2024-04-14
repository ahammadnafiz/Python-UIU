import math

prime_powers = {}

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for i in range(2, n + 1):
    if is_prime(i):
        pow_list = []
        for j in range(3, int(math.sqrt(100)) + 1):
            power = i ** j
            if power <= 100 and int(math.sqrt(power)) ** 2 != power:
                pow_list.append(power)
        if pow_list:
            prime_powers[i] = pow_list

print(prime_powers)
