num_1, opr, num_2 = list(map(str, input().split()))

num_1, num_2 = float(num_1), float(num_2)

if opr == "+":
    print(f"Addision is {num_1 + num_2}")
elif opr == "-":
    print(f"Substraction is {num_1 - num_2}")
elif opr == "*":
    print(f"Multiplication: {num_1 * num_2}")
elif opr == "/":
    if num_2 == 0:
        print("Division: Zero as divisor is not valid")
    else:
        print(f"Division: {num_1/num_2}")
else:
    print("Unknown operator")
