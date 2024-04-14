def Get_Number_And_Base ():
    
    while True:
        try:
            N, B = [int(i) for i in input().split()]
            if 2 <= B <= 16:
                return N, B
            else:
                print("Base not within proper range!")
        except ValueError:
            print("Invalid input. Please enter valid integers.")
    
def convert_number(number, base):
    if number == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    result = ""
    
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base
    
    return result

def show_converted_number(converted_number):
    print(converted_number)

def main():
    number, base = Get_Number_And_Base()
    converted_number = convert_number(number, base)
    show_converted_number(converted_number)

if __name__ == "__main__":
    main()