class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self._items = [None]*self.capacity
        self.top = -1

    def push(self, item):
        if self.top == self.capacity - 1:
            raise Exception("StackOverflow")

        self.capacity += 1
        self._items[self.top] = item

    def pop(self):
        if self.top == -1:
            raise Exception("StackUnderflow")

        item = self._items[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")

        return self._items[self.top]
