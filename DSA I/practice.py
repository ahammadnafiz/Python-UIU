class Stack:
    def __init__(self, capacity=None):
        self._items = [] # Initialize an empty Stack
        self.capacity = capacity

    def push(self, item):
        if self.capacity and len(self._items) >= self.capacity:
            raise StackOverflowError("Stack is at capacity")

        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def is_full(self):
        return self.capacity is not None and len(self._items) >= self.capacity

    def size(self):
        return len(self._items)

    def clear(self):
        self._items = []

    def to_list(self):
        return self._items.copy()

    def __str__(self):
        return f"Stack({self._items})"

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __getitem__(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of range")
        return self._items[index]

class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass


def match_pairs(pairs):
    left = '([{'
    right = ')]}'
    stack = Stack()
    
    for char in pairs:
        if char in left:
            stack.push(char)
        elif char in right:
            if stack.is_empty():
                return False

            right_index = right.index(char)
            matching_left = left[right_index]

            if stack.pop() != matching_left:
                return False

    return stack.is_empty()

print(match_pairs("[(])"))
