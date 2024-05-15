### Infinite Iterators

1. **`count(start=0, step=1)`**:
   - Generates an infinite sequence of numbers starting from `start` with a specified `step`.
   ```python
   import itertools

   counter = itertools.count(start=10, step=2)
   print(next(counter))  # Output: 10
   print(next(counter))  # Output: 12
   ```

2. **`cycle(iterable)`**:
   - Repeats the elements of `iterable` indefinitely.
   ```python
   import itertools

   colors = itertools.cycle(['red', 'green', 'blue'])
   print(next(colors))  # Output: 'red'
   print(next(colors))  # Output: 'green'
   ```

3. **`repeat(elem, times=None)`**:
   - Returns the element `elem` `times` number of times, or indefinitely if `times` is `None`.
   ```python
   import itertools

   repeated = itertools.repeat(10, times=3)
   print(list(repeated))  # Output: [10, 10, 10]
   ```

### Iterators Terminating on the Shortest Input Sequence

4. **`accumulate(iterable, func=operator.add)`**:
   - Returns an iterator that yields accumulated sums (or results of other binary functions) of elements in `iterable`.
   ```python
   import itertools
   import operator

   data = [1, 2, 3, 4, 5]
   accumulated = itertools.accumulate(data)
   print(list(accumulated))  # Output: [1, 3, 6, 10, 15]
   ```

5. **`chain(*iterables)`**:
   - Chains together multiple iterables into a single sequence.
   ```python
   import itertools

   letters = itertools.chain('ABC', 'DEF')
   print(list(letters))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
   ```

6. **`chain.from_iterable(iterables)`**:
   - Chains together a sequence of iterables into a single sequence.
   ```python
   import itertools

   data = [[1, 2], [3, 4], [5, 6]]
   flattened = itertools.chain.from_iterable(data)
   print(list(flattened))  # Output: [1, 2, 3, 4, 5, 6]
   ```

7. **`compress(data, selectors)`**:
   - Returns elements from `data` where corresponding elements in `selectors` are true.
   ```python
   import itertools

   data = ['a', 'b', 'c', 'd']
   selectors = [True, False, True, False]
   filtered = itertools.compress(data, selectors)
   print(list(filtered))  # Output: ['a', 'c']
   ```

8. **`dropwhile(predicate, iterable)`**:
   - Drops elements from the iterable while the predicate is true, then returns the rest.
   ```python
   import itertools

   data = [1, 3, 5, 7, 2, 4, 6, 8]
   filtered = itertools.dropwhile(lambda x: x < 5, data)
   print(list(filtered))  # Output: [5, 7, 2, 4, 6, 8]
   ```

9. **`takewhile(predicate, iterable)`**:
   - Returns elements from the iterable while the predicate is true, then stops.
   ```python
   import itertools

   data = [1, 3, 5, 7, 2, 4, 6, 8]
   filtered = itertools.takewhile(lambda x: x < 5, data)
   print(list(filtered))  # Output: [1, 3]
   ```

10. **`filterfalse(predicate, iterable)`**:
    - Returns elements from the iterable where the predicate returns false.
    ```python
    import itertools

    data = [1, 2, 3, 4, 5]
    filtered = itertools.filterfalse(lambda x: x % 2 == 0, data)
    print(list(filtered))  # Output: [1, 3, 5]
    ```

### Combinatoric Generators

11. **`product(*iterables, repeat=1)`**:
    - Computes the Cartesian product of input iterables.
    ```python
    import itertools

    colors = ['red', 'green']
    shapes = ['circle', 'square']
    combinations = itertools.product(colors, shapes)
    print(list(combinations))  # Output: [('red', 'circle'), ('red', 'square'), ('green', 'circle'), ('green', 'square')]
    ```

12. **`permutations(iterable, r=None)`**:
    - Generates all possible r-length permutations of elements in the iterable.
    ```python
    import itertools

    perms = itertools.permutations('ABCD', 2)
    print(list(perms))  # Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
    ```

13. **`combinations(iterable, r)`**:
    - Generates all possible r-length combinations of elements in the iterable.
    ```python
    import itertools

    combs = itertools.combinations('ABCD', 2)
    print(list(combs))  # Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    ```

14. **`combinations_with_replacement(iterable, r)`**:
    - Generates all possible r-length combinations of elements in the iterable with replacement.
    ```python
    import itertools

    combs_rep = itertools.combinations_with_replacement('ABCD', 2)
    print(list(combs_rep))  # Output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]
    ```
