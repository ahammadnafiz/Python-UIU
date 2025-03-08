print(
    """
    There are Four Choices:

    1 -> Addition
    2 -> Substraction
    3 -> Multiplication
    4 -> Division

    """
)

num_1, num_2 = map(float, input().split())
choice = int(input())

if choice == 1:
    print(f"Addition: {num_1 + num_2}")
elif choice == 2:
    print(f"Substraction: {num_1 - num_2}")
elif choice == 3:
    print(f"Multiplication: {num_1 * num_2}")
elif choice == 4:
    if num_2 != 0:
        case = int(input())
        if case == 1:
            print(f"Quotient: {num_1 // num_2}")
        elif case == 2:
            print(f"Reminder: {num_1 % num_2}")
        else:
            print("Unknown case")
    else:
        print("Error: Divisor is zero")
