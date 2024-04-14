n = int(input())
results = []

for i in range(n):
    user = list(map(float, input().split()))
    results.append(user[-1])

count = 1
for result in results:
    if 90 <= result <= 100:
        print(f"Student {count}: A")
    elif 86 <= result <= 89:
        print(f"Student {count}: A-")
    elif 82 <= result <= 85:
        print(f"Student {count}: B+")
    elif 78 <= result <= 81:
        print(f"Student {count}: B")
    elif 74 <= result <= 77:
        print(f"Student {count}: B-")
    elif 70 <= result <= 73:
        print(f"Student {count}: C+")
    elif 66 <= result <= 69:
        print(f"Student {count}: c")
    elif 62 <= result <= 65:
        print(f"Student {count}: C-")
    elif 58 <= result <= 61:
        print(f"Student {count}: D+")
    elif 55 <= result <= 57:
        print(f"Student {count}: D")
    elif 0 <= result < 55:
        print(f"Student {count}: F")