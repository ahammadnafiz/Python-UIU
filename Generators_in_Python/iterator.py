# What is Iteration
'''
Iteration is a general term for taking item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, this is Iteration. It's the process
'''

# Example
num = [1, 2, 3]
for i in num:
    print(i)

# What is Iterator
'''
An Iterator is an object that allows the programmer to traverse through a
sequence of data without having to store the entire data in memory
With the help of Iterator, Iteration procced
'''

# Example
my_list = [i for i in range(1,100000000)]   # In this Example it first create a list and save it to memory

# Suppose we want to multiply all the item by 2

'''
for i in my_list:   # that's not memory efficient
    print(i*2)   
'''

# If we get the size of the list
import sys
print(sys.getsizeof(my_list)/1024)  # That was 815555 kb


# Same thing but different way
x = range(1,100000000)
print(sys.getsizeof(x)/1024)    # 0.046875kb

# That was the difference, the Iterator object doesn't store the item in the memory, ratherthan it perform task one by one

# What is Iterable

'''
Iterable is an object, which one can iterate over.
It generates an Iterator when passes to iter() method
In simple word, if we perform loop on that object it's Iterable
'''

# Example

L = [1, 2, 3, 4]
print(type(L))              # L --> is an Iterable object
print(iter(L))              # iter(L) --> Iterator


# Points to remember
'''
Every Iterator is also an Iterables
Not all Iterables are Iterators
'''

'''
Like we saw the previous Example's where we create list that's an Iterable object but not Iterators because List save's item data in the memory. Thus list is an Iterable not Iterators
'''

# Tricks
'''
Every Iterable has an __iter__() function
Every Iterator has both __iter__() function as well as a __next__() function
'''

# Example
a = 2

# If we pass to dir function we can see there is no iter function, cz it's not an Iterable object

print(dir(a))

my_tuple = (1, 2, 3)
print(dir(my_tuple))    # It have __iter__ function but no __next__ function because it's not an Iterator

# But we can convert any Iterable object which is not Iterator by passing it to iter() function

print(type(iter(my_tuple)))     # my_tuple -->tuple_iterator


# Understanding how for loop works

my_list = [2, 3, 4, 5]

# Step 1 --> Fetch the Iterator

iter_num = iter(my_list)

# Step 2 --> next(), tell me the state of the Iterator

print(next(iter_num))   # Output: 2
print(next(iter_num))   # Output: 3
print(next(iter_num))   # Output: 4
print(next(iter_num))   # Output: 5
#print(next(iter_num))   # StopIteration error bcz we have 4 items


# Making our own for loop
def our_for_loop(iterable):
    # Step 1 -->  Fetch iterable
    iterator = iter(iterable)
    
    # Step 2 --> next()
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

# Test our own for loop

a = [1, 2, 3]
our_for_loop(a)


# Let's Create our own range() function

# Iterable
class OurRangeIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return OurRangeIterator(self)

# Iterator
class OurRangeIterator:
    def __init__(self, iterable_object):
        self.iterable = iterable_object
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration

        current = self.iterable.start
        self.iterable.start += 1
        return current

# Create an object
z = OurRangeIterable(2, 10)
for i in z:
    print(i)
