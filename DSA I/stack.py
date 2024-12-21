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

# Example usage:
if __name__ == "__main__":
    stack = Stack(capacity=3)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Stack: {stack}")  # Stack([1, 2, 3])
    print(f"Size: {stack.size()}")  # Size: 3
    print(f"Top item: {stack.peek()}")  # Top item: 3

    print(f"Item at index 1: {stack[1]}")  # Item at index 1: 2

    popped = stack.pop()
    print(f"Popped: {popped}")  # Popped: 3
    print(f"New stack: {stack}")  # New stack: Stack([1, 2])

    print(f"Is empty? {stack.is_empty()}")  # Is empty? False

    stack.clear()
    print(f"After clear: {stack}")  # After clear: Stack([])
