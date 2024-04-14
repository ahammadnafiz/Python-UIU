class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        real_sum = self.real_part + other.real_part
        imaginary_sum = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real_part - other.real_part
        imaginary_diff = self.imaginary_part - other.imaginary_part
        return ComplexNumber(real_diff, imaginary_diff)

    def __mul__(self, other):
        real_product = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        imaginary_product = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
        return ComplexNumber(real_product, imaginary_product)

    def __str__(self):
        return f"{self.real_part} + {self.imaginary_part}i"

# Example usage:
complex_num1 = ComplexNumber(3, 4)
complex_num2 = ComplexNumber(1, 2)

# Addition
result_addition = complex_num1 + complex_num2
print("Addition:", result_addition)

# Subtraction
result_subtraction = complex_num1 - complex_num2
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = complex_num1 * complex_num2
print("Multiplication:", result_multiplication)
