def letters_generator():
    yield 'a'
    yield 'b'
    yield 'c'

def numbers_generator():
    yield 1
    yield 2
    yield 3

def combined_generator():
    letters = letters_generator()
    numbers = numbers_generator()
    
    try:
        while True:
            yield next(letters)
            yield next(letters)
            yield next(numbers)
    except StopIteration:
        yield 'End of sequence'

for i in combined_generator():
    print(i)

# Output
'''
a
b
1
c
End of sequence
'''
