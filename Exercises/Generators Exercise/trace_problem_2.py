def filter_generator(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield item

even_numbers = filter_generator(lambda x: x % 2 == 0, range(10))

for i in even_numbers:
    print(i)
