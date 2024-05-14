'''
Write a Python program to implement a generator function that generates all permutations of a given list of elements.
'''

def permutation_generator(elements):
    n = len(elements)
    if n <= 1:
        yield elements
    else:
        for i in range(n):
            first_element = elements[i]
            rest_element = elements[:i] + elements[i + 1:]
            for perm in permutation_generator(rest_element):
                yield [first_element] + perm

elements = [1, 2, 3]

perms = permutation_generator(elements)

for perm in perms:
    print(perm)
