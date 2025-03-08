ch = input("Enter a character: ")

if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
    print("Alphabet")
elif "0" <= ch <= "9":
    print("Digit")
else:
    print("Special")
