def outer_gen(n):
    def inner_gen(m):
        for i in range(m):
            yield i**2
    for j in range(n):
        yield inner_gen(j+1)

result = [y for x in outer_gen(3) for y in x]
print(result)

# Output
'''
0, 0, 1, 0, 1, 4
'''
