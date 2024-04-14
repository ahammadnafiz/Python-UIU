n = int(input())

prev = 1
result = prev

for i in range(2, n + 1):
    prev = (prev * 10) + i
    result += prev

print(result)