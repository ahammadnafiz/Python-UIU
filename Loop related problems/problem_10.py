n = int(input())

result = []

for i in range(1, n + 1):
    if i % 2 == 0:
        result.append(-i)
    else:
        result.append(i)

print(f"Result: {sum(result)}")