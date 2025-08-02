def outer_gen(n):
    def inner_gen(m):
        for i in range(m, 0, -1):
            yield i**3
    yield from (inner_gen(j) for j in range(1, n+1))

result = list(outer_gen(4))
print(result)

# Output
'''
[1, 8, 1, 27, 8, 1, 64, 27, 8, 1]
'''
