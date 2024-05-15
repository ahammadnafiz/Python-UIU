def nested_generator():
    for i in range(3):
        yield i
        yield from ('abc'[i] for _ in range(i+1))
nest = nested_generator()
for i in nest:
    print(i)

# Output
'''
0
a
1
b
b
2
c
c
c
'''
