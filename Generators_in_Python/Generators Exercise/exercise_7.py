def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(range_num):
    num = 2
    count = 0
    
    while True:
        if is_prime(num):
            yield num
            count += 1
            if count == range_num:
                break
        num += 1

nums = prime_generator(10)
for i in nums:
    print(i)
