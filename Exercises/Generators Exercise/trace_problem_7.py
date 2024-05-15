def filtered_pipeline(lst):
    def is_even(x):
        return x % 2 == 0
    
    def square(x):
        return x ** 2
    
    def transform(x):
        if is_even(x):
            return square(x)
        else:
            return None
    
    for num in lst:
        result = transform(num)
        if result is not None:
            yield result

# Output
'''
[4, 16]
'''
