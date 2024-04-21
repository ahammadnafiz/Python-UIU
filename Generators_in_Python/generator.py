# Python generatos are a simple way of creating iterators

# Example
def gen_demo():     # There is not return statement in generatos
    yield 'First Statement'
    yield 'Second Statement'
    yield 'Third Statement'

gen = gen_demo()
print(gen)      # Generator object

# Using the next() function we can get the information holing yieldone by one

print(next(gen))    # First Statement
print(next(gen))    # Second Statement
print(next(gen))    # Third Statement
#print(next(gen))    # StopIteration error

# Example
def square(num):
    for i in range(1, num+1):
        yield i**2

gen = square(10)
print(next(gen))    # 1
print(next(gen))    # 4
print(next(gen))    # 9
# Here is the interesting part the loop continued form the last state of next() where it yield it's value

# Start form 4
for i in gen:
    print(i)    # Then 16.. continued

# Range Function Using Generator
def my_range(start, end):
    for i in range(start, end):
        yield i

for i in my_range(20, 30):
    print(i)

# Generator Expression
gen = (i for i in range(4))     # Using First brackets

# Representing Infinite Streams
def all_even():
    n = 0
    while True:
        yield n
        n += 2

gen = all_even()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 2
print(next(gen))  # Output: 4
# ... and so on

# Chaining Generators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))  # Output: 4895
