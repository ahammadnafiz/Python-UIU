n = int(input())
original_n = n
r_n = 0

while n > 0:
    l_d = n % 10
    r_n = (r_n * 10) +  l_d
    n //= 10

formated_rn = f'{r_n:0{len(str(n))}}'

if original_n == int(formated_rn):
    print('Yes')
else:
    print('No')