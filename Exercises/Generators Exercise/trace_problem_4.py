def range_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

def filter_generator(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield item

def conditional_combined_generator(n):
    numbers = range_generator(n)
    filtered_numbers = filter_generator(lambda x: x % 2 == 0, numbers)
    
    try:
        while True:
            value = next(filtered_numbers)
            if value < 5:
                yield f"Small: {value}"
            else:
                yield f"Large: {value}"
    except StopIteration:
        yield "End of sequence"

for i in conditional_combined_generator(10):
    print(i)
