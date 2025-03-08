print(
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][
        int(n)
    ]
    if (n := input("Enter a single-digit number: ")).isdigit() and len(n) == 1
    else "Invalid input!"
)
